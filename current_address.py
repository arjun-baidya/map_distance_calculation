import requests
r  = requests.get('https://get.geojs.io/')
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ip_address = ip_request.json()['ip']
print("ip address", ip_address)

url = 'https://get.geojs.io/v1/ip/geo/'+ip_address+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()
print(geo_data)

city = geo_data['city']
region = geo_data['region']
country = geo_data['country']
time_zone = geo_data['timezone']
latitude = geo_data['latitude']
longitude = geo_data['longitude']

print("city    :", city)
print('region   :', region)
print('country   :', country)
print('time zone  :', time_zone)
print('latitude  :', latitude)
print('longitude  :', longitude)