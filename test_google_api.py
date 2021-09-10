import config
import googlemaps
import json

API_KEY = config.get_gmap_api_key()

gmaps = googlemaps.Client(key=API_KEY)

query = "San Jose State University"
result_JSON = gmaps.places(query)
# print(json.dumps(result_JSON,indent=2))

print(result_JSON['results'])
street_string, location_string, country_string = result_JSON['results'][0]['formatted_address'].split(", ")

print(f"Query: {query} - Address: {street_string}, {location_string}, {country_string}")