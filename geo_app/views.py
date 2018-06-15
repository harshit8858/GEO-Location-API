from django.shortcuts import render
import requests
from django.views.decorators.debug import sensitive_variables


@sensitive_variables('data')
def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    r = requests.get('http://freegeoip.net/json/%s' % ip_address)
    data = r.json()

    return render(request, 'geo_app/geo_ip.html', {'ip':data['ip'], 'country':data['country_name'], 'lat':data['latitude'], 'lon':data['longitude'], 'api':'AIzaSyBx6vrcFlszZb8kxjGhylF5nteLki4N8Nw' })