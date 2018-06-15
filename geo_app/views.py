from django.shortcuts import render
import requests


def home(request):
    r = requests.get('http://freegeoip.net/json/')
    data = r.json()

    return render(request, 'geo_app/geo_ip.html', {'ip':data['ip'], 'country':data['country_name']})