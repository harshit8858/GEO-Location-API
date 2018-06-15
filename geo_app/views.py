from django.shortcuts import render
import requests
from django.views.decorators.debug import sensitive_variables


@sensitive_variables('data')
def home(request):
    is_cached = ('data' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        r = requests.get('http://freegeoip.net/json/%s' % ip_address)
        # data = r.json()
        request.session['data'] = r.json()

    data = request.session['data']
    # x = YOUR_API_KEY      # get you apikey, go to developers.google.com/maps/web/ and click on “Get a Key”, generate an API for yourself.

    return render(request, 'geo_app/geo_ip.html', {'ip':data['ip'],
                                                   'country':data['country_name'],
                                                   'lat':data['latitude'],
                                                   'lon':data['longitude'],
                                                   'api':'AIzaSyBx6vrcFlszZb8kxjGhylF5nteLki4N8Nw',
                                                   'is_cached':is_cached })
    # return render(request, 'geo_app/geo_ip.html', {'ip':data['ip'], 'country':data['country_name'], 'lat':data['latitude'], 'lon':data['longitude'], 'api':x })