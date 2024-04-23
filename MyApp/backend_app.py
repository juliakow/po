from flask import Flask, request, jsonify
from air_quality_client import AirQualityClient
from data_validation import validate_temperature, validate_pressure, validate_humidity

app = Flask(__name__)
client = AirQualityClient()

@app.route('/airquality', methods=['GET'])
def get_air_quality():
    data = client.get_air_quality_data()

    # walidacja temaperatury
    try: validate_temperature(data.get('temperature'))
    except ValueError as e:
        return jsonify({"error": str()}), 400
    
    # walidacja cisnienia
    try:
        validate_pressure(data.get('pressure'))
    except ValueError as e:
        return jsonify({"error": str(e)}),  400
    
    # walidacja wilgotnosci
    try:
        validate_humidity(data.get('himidity'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug = True)