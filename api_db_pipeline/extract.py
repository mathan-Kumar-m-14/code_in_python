import requests

weather_url='https://api.open-meteo.com/v1/forecast'
geocoding_url='http://api.openweathermap.org/geo/1.0/direct'
api_keys='a245a58babf3ba9a7ddf9622bf68ae2a'


def getgeocoding(name):
    frame_api_params={'q':name,'limit':1,'appid':api_keys}
    try:
        response_geocode=requests.get(geocoding_url,params=frame_api_params,timeout=10)

        #if response_geocode.status_code==200:
        response_geocode.raise_for_status()
        data_geocode = response_geocode.json()

        if data_geocode:
            lat_code = data_geocode[0]['lat']
            lon_code = data_geocode[0]['lon']
            return lat_code,lon_code
        print(f'Data Not available for the {name}')
        return None,None
        # else:
            # print(f'{response_geocode} : Geocode Data Not Received')
    except requests.exceptions.Timeout:
        print('Geocode request timed out')
    except requests.exceptions.ConnectionError:
        print('Network error: could not connect to geocoding API')
    except requests.exceptions.HTTPError as e:
        print(f'Geocode API returned an error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Unexpected request error: {e}')
    return None,None


def getweather_info(code1, code2):
    frame_weather_api_params = {"latitude": code1,"longitude": code2,
                                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                                "timezone": "auto"
                               }
    try:
        response_weather_data = requests.get(weather_url, params=frame_weather_api_params,timeout=10)
        response_weather_data.raise_for_status()
        return response_weather_data.json()

    except requests.exceptions.Timeout:
        print('Weather API request timed out')
    except requests.exceptions.ConnectionError:
        print('Network error: could not connect to Weather API')
    except requests.exceptions.HTTPError as e:
        print(f'Weather API returned an error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Unexpected request error: {e}')
    return None









