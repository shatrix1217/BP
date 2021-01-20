#geocoding API
import os, requests
from urllib.parse import urlencode

api_key = os.environ.get('GCP_api_key')

data_type = "json"
endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
#sample from google maps platform doc
params = {"adress" : "1600 Amphitheatre Parkway, Mountain View, CA", "key" : api_key}
url_params = urlencode(params)
sample = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY"

url = f"{endpoint}?{url_params}"

def extract_lat_lng(adress_or_postal_code, data_type = "json"):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"adress" : adress_or_postal_code, "key" : api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return{}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")