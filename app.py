import json
import urllib
url = "http://api.openweathermap.org/data/2.5/forecast?id=3155573&APPID=0aa43b6005881a082d2282b698788d1c"
response = urllib.urlopen(url)
data = json.loads(response.read())
#json_data = response.json()
print data
