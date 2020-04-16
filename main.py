import requests
from data import Location, WeatherElement

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)

json_content = html_content.json()

records = json_content.get('records')
location = records.get('location')

locations = []

for l in location:
    print(l)
    location_site = Location()
    location_site.from_json(l)
    locations.append(location_site)
