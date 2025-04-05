from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse, StreamingResponse

from app.repositories import ParameterRepository
from .models import SpeechRequest, ParameterUpdate
from .services import SpeechService
from .dependencies import get_speech_service, get_parameter_repository
import io

app = FastAPI()

@app.post("/to_speech")
async def text_to_speech(
    request: SpeechRequest,
    speech_service: SpeechService = Depends(get_speech_service)
):
    try:
        audio_content = speech_service.text_to_speech(request.text, request.output_filename)
        
        if request.output_filename:
            return StreamingResponse(
                io.BytesIO(audio_content),
                media_type="audio/wav",
                headers={"Content-Disposition": f"attachment; filename={request.output_filename}"}
            )
        else:
            return {"status": "Speech played successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/set_parameter")
async def set_parameter(
    update: ParameterUpdate,
    param_repo: ParameterRepository = Depends(get_parameter_repository)
):
    param_repo.set_parameter(update.parameter_name, update.parameter_value)
    return {"status": "Parameter updated successfully"}

@app.get("/parameters")
async def get_parameters(
    param_repo: ParameterRepository = Depends(get_parameter_repository)
):
    return param_repo.get_all_parameters()