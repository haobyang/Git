class Location:
    def __init__(self, location_name=None,lat=None,lon=None,station_id=None,time=None,weather_element=None):

        self.locationName = location_name
        self.lat = lat
        self.lon = lon
        self.stationID = station_id
        self.time = time
        self.weatherElement = weather_element

    def from_json(self,json_data):

        self.locationName = json_data.get('locationName')
        self.lat = json_data.get('lat')
        self.stationID = json_data.get('stationId')
        self.time = json_data.get('time').get('obsTime')

        self.weatherElement = WeatherElement()
        self.weatherElement.from_json(json_data['weatherElement'])
        # print(json_data)

class WeatherElement:
    def __init__(self,wdir=None,wdsd=None,temp=None,humd=None,h_24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h_24r = h_24r

    def from_json(self, weather_element):
        for element in weather_element:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')

            if element_name == 'WDIR':
                self.wdir = element_value

            if element_name == 'WDSD':
                self.wdsd = element_value

            if element_name == 'TEMP':
                self.temp = element_value

            if element_name == 'HUMD':
                self.humd = element_value

            if element_name == '24R':
                self.h_24r = element_value

