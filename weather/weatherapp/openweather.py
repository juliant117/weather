import requests
import json
from datetime import datetime, timedelta

def get_weather_forecast(city, api_key):


    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"  # Use metric units
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

        forecast_list = []
        for i in range(0, len(data['list']), 8): # OpenWeatherMap returns forecast every 3 hours. 8*3 = 24 hours
            daily_data = data['list'][i]
            date_str = daily_data['dt_txt'][:10]  # Get date string (YYYY-MM-DD)
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            
            # Get max and min temperatures for the day
            max_temp = -100 # Initialize with a very low value
            min_temp = 100  # Initialize with a very high value

            for j in range(i, i+8):
                if j < len(data['list']): # Check if index is within the list
                    temp = data['list'][j]['main']['temp']
                    max_temp = max(max_temp, temp)
                    min_temp = min(min_temp, temp)

            conditions = data['list'][i]['weather'][0]['description']

            forecast_list.append({
                'date': date_obj.strftime('%Y-%m-%d'),  # Format the date
                'max_temp': max_temp,
                'min_temp': min_temp,
                'conditions': conditions
            })
        #print(forecast_list)

        return forecast_list

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except (KeyError, IndexError) as e: # Handle potential JSON errors
        print(f"Error processing JSON: {e}")
        return None
