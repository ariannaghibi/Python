from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=d0ecb00959e8f61362398bb7cebd40fa'
    err_msg = ''
    message = ''
    message_color_class = ''
    # This if statement is used when the user submits the form to send data to a server to update it.
    if request.method == 'POST':
        form = CityForm(request.POST)
        # This if statement will first validate the form. Then it gets the name of the city from
        # the form. Finally it counts to see if the city name is already in the City table or not
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            # If count is zero, that means the city hasn't been added yet.
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                # If you print 'r', you will see the 'cod' number for invalid city is 404 and for valid city is 200
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = "ERROR: City does not exist in the world!"
            else:
                err_msg = "ERROR: City already exists in the database!"

        if err_msg:
            message = err_msg
            # From the CSS file that has been referenced in the html file, '.notification.is-danger' class will create a red box
            message_color_class = 'is-danger'
        else:
            message = 'City added successfully'
            # From the CSS file that has been referenced in the html file, '.notification.is-success' class will create a green box
            message_color_class = 'is-success'

    # Restart the form after the user adds the city
    form = CityForm()

    cities = City.objects.all()
    weather_data = []

    # for every city in the given table of cities, the weather forecast information will be assigned to each and stored in a list
    for city in cities:
        r = requests.get(url.format(city)).json()
        # print 'r' to see output of the requests, which can be
        # used to define the dictionary below
        city_weather = {
            'city': city.name,
            'country': r['sys']['country'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
            'wind': r['wind']['speed']
        }
        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_color_class': message_color_class
    }
    # render template to the app by feeding the given context
    return render(request, 'weather.html', context)


# This function will delete the city from the database and redirects the url to home page
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')
