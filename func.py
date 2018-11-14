from geopy.geocoders import Nominatim
import pandas as pd
import re


def generate_batch(name='', batch_size=1, testing=False):
    geo_locator = Nominatim(user_agent='Phase_App')

    batch = geo_locator.geocode(name, exactly_one=testing, limit=batch_size, addressdetails=True)
    block = []
    coords = []

    for line in batch:
        line_data = line.raw
        line_coord = {'lat/lon': [line_data['lat'], line_data['lon']]}

        address_data = line_data['address']
        address_headers = list(line_data['address'].keys())

        try:
            address_data['name'] = address_data.pop(address_headers[0])
        except KeyError:
            print("error")

        block.append(address_data)
        coords.append(line_coord)

        print(line_data)

    address_frame = pd.DataFrame.from_records(block, index=None)
    coord_frame = pd.DataFrame.from_records(coords)

    result_frame = address_frame.join(coord_frame)
    result_frame = result_frame.fillna('NaN')

    return result_frame


def load_biznames():
    with open('Business_Names.txt', encoding='utf-8') as file:
        biz_names = [line.strip() for line in file]

    return biz_names

# df = pd.DataFrame.from_records(block,index=None)
