from django.contrib import messages
from django.shortcuts import render
import requests
import datetime

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Delhi'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d8fbcdea56fc17173f7bae697b42630'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyAblt1O3Un64mASY4p9GEBRygHxc40d-bY'
    SEARCH_ENGINE_ID = '103b36d31bd204c1e'

    query= city +"1920x1080"
    page=1
    start = (page-1)*10+1
    searchType = 'image'
    city_url= f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType={searchType}&start={start}&searchType={searchType}&imgSize=xlarge'

    data= requests.get(city_url).json()
    count=1
    search_items= data.get('items')
    image_url= search_items[1]['link']

    try:
        data= requests.get(url,PARAMS).json()

        description= data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day= datetime.date.today()

        return render(request,'index.html',{'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city, 'exception_occured': False, 'image_url':image_url})
    except:
        exception_occured = True
        messages.error(request, 'City not found')
        day= datetime.date.today()

        return render(request,'index.html',{'description':'clear sky', 'icon':'01d', 'temp':25, 'day':day, 'city':'delhi','exception_occured': True})
    
