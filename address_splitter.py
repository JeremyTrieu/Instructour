#%%
import config
import googlemaps
import json

def gmaps_address_splitter(string: str, gmaps: googlemaps.client.Client) -> dict:
    """This functions takes in a address string input and googlemaps.client.Client variable. 

    Args:
        string (str): Example: 15 Broadway, Ultimo NSW 2007, Australia
                               124 La Trobe St, Melbourne VIC 3000

        gmaps (googlemaps.client.Client): require googlemaps api

    Returns:
        ADDRESS_DICT dict: an address dict containing street, city, state, postcode and country
    """
    import re
    
    pattern = r".+?(?=\s\w+\s\d.*$)"
    temp_address_list = string.split(", ")
    address_list = []

    for i, address in enumerate(temp_address_list):
        if len(temp_address_list) == 4 and i == 2:
            location_list = address.split(" ")
            address_list.extend(location_list)
            continue

        elif len(temp_address_list) in [3, 2]:
            if i == 1:
                result_regex = re.search(pattern, address)
                if result_regex:
                    city = result_regex.group()
                    state_postcode_list = address.replace(city+" ","").split(" ")
                    state = state_postcode_list[0]
                    postcode = state_postcode_list[1]
                    address_list.extend([city, state, postcode])

                if len(temp_address_list) == 2:
                    result_JSON = gmaps.places(city)
                    country_address_list = result_JSON['results'][0]['formatted_address']
                    for element in country_address_list.split(", "):
                        if len(element.split(" ")) == 1:
                            address_list.append(element)
                            break
                continue

        address_list.append(address)

    return {
        "Street":address_list[0],
        "City":address_list[1],
        "State":address_list[2],
        "Postcode":address_list[3],
        "Country":address_list[4]
    }

API_KEY = config.get_gmap_api_key()
gmaps = googlemaps.Client(key=API_KEY)
#%%

query = 'MIT'
result_JSON = gmaps.places(query)

test_string_1 = "15 Broadway, Ultimo NSW 2007, Australia"
test_string_2 = "1 Washington Sq, San Jose, CA 95192, United States"
test_string_3 = "124 La Trobe St, Melbourne VIC 3000"
#%%
ADDRESS_DICT = gmaps_address_splitter(result_JSON['results'][0]['formatted_address'], gmaps)
print(ADDRESS_DICT)
# %%
