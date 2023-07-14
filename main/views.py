from django.shortcuts import render
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired, use your own api_key
            place api_key in place of appid="your api_key here" '''

        # source contains json data from the API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        # converting json data to dictionary

        list_of_data = json.loads(source)

        # convert temperature from Kelvin to Celsius
        temp_kelvin = float(list_of_data['main']['temp'])
        temp_celsius = temp_kelvin - 273.15  # conversion formula

        # data for the template
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(round(temp_celsius, 2)) + '°C',  # display temperature in Celsius with 2 decimal places
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
