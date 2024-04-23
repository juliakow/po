def validate_temperature(temperature):
    if not isinstance(temperature, (int, float)):
        raise ValueError("temperature must be a number")
    if temperature < -100 or temperature > 100:
        raise ValueError("temperature out of range")
    

def validate_pressure(pressure):
    if not isinstance(pressure, (int, float)):
        raise ValueError("Pressure must be a number")
    if pressure < 500 or pressure > 1100:
        raise ValueError("Pressure out of range")


def validate_humidity(humidity):
    if not isinstance(humidity, (int, float)):
        raise ValueError("Humidity must be a number")
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity out of range")