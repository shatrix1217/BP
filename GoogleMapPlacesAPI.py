#places API
import os, requests
from urllib.parse import urlencode

api_key = os.environ.get('GCP_api_key')

lat, lng = 37.42230960000001, -122.0846244 #geocode from google maps platform doc demo
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params = {
    "key" : api_key,
    "input" : "Udon",
    "inputtype" : "textquery",
    "fields" : "formatted_address,name,geometry"
}
locationbias = f"point:{lat}, {lng}"
use_circular = False
if use_circular :
    radius = 1000
    locationbias = f"circle:{radius}@{lat}, {lng}"

params["locationbias"] = locationbias

params_encoded = urlencode(params)
places_endpoint = f"{base_endpoint_places}?{params_encoded}"

r = requests.get(places_endpoint)
r.json()