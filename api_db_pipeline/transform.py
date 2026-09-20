import math
def getweatherdetails(city,json_data):
    try:
        data_dict={
                   "city"           : city,
                   "timezone"       : json_data['timezone'],
                   "time"           : json_data['current']['time'],
                   "temperature"    : json_data['current']['temperature_2m'],
                   "humidity"       : json_data['current']['relative_humidity_2m'],
                   "wind speed"     : json_data['current']['wind_speed_10m']
        }
    except KeyError as e:
        print(f'Missing expected field in weather data: {e}')
        return None


    if data_dict:
        def check_weather_logic(temperature_c, humidity_percentage):
            """
            Determines if the weather condition is 'Hot', 'Rainy/Saturated', or 'Normal'.
            Uses Celsius for temperature.
            """
            # 1. Calculate Dew Point using the Magnus-Tetens approximation
            # This helps determine how close the air is to raining
            a = 17.27
            b = 237.7
            alpha = ((a * temperature_c) / (b + temperature_c)) + math.log(humidity_percentage / 100.0)
            dew_point = (b * alpha) / (a - alpha)

            # 2. Simple Heat Index Approximation (Rothfusz regression equivalent for metric)
            # Converts to Fahrenheit briefly for standard NWS formula thresholding
            temp_f = (temperature_c * 9 / 5) + 32

            # Simple heat index formula for quick logic check
            heat_index_f = 0.5 * (temp_f + 61.0 + ((temp_f - 68.0) * 1.2) + (humidity_percentage * 0.094))
            heat_index_c = (heat_index_f - 32) * 5 / 9

            # 3. Decision Logic Matrix
            data_dict['is_rainy']=humidity_percentage >= 90 and (temperature_c - dew_point) <= 2
            data_dict['is_hot']  =temperature_c >= 27 and heat_index_c >= 32

            return None

        check_weather_logic(temperature_c= data_dict['temperature'],humidity_percentage= data_dict['humidity'])
    return data_dict


