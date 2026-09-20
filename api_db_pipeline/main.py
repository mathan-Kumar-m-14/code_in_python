from extract import getgeocoding
from extract import getweather_info
from transform import getweatherdetails
from load import fn_saveoperation

if __name__=='__main__':
    cityname=input('Enter the City Name:')
    if cityname.isalpha():
        lat_code, lon_code = getgeocoding(cityname)
        if lat_code and lon_code:
            print(f'City: {cityname}, lat: {lat_code}, lon: {lon_code}')
            weather_details = getweather_info(lat_code, lon_code)
            if weather_details:
                structured_data=getweatherdetails(cityname,weather_details)
                if structured_data:
                    status=fn_saveoperation(structured_data)
                    print(status)
    else:
        print('Please enter the valid City name')



