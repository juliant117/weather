import requests
import json

def get_weather_data(city):
  api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual key
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric" # Example URL (adjust as needed)

  response = requests.get(url)

  if response.status_code == 200: # Check for successful response
    data = response.json()  # Parse the JSON response
    # ... (Extract the data you need from the 'data' dictionary) ...
    return extracted_data # Return the extracted data
  else:
    print("Error fetching weather data")
    return None

# In your Django view:
def my_weather_view(request):
    city = "London" # Get city from user input or however you want to specify it.
    weather_data = get_weather_data(city)
    if weather_data:
        # Pass weather_data to your template
        return render(request, 'my_template.html', {'weather': weather_data})
    else:
      return render(request, 'error.html') #handle the error.