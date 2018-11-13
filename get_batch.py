from geopy.geocoders import Nominatim
import pandas as pd

def generate_batch(name='', batch_size=1, testing=False):
    geo_locator = Nominatim(user_agent='Phase_App')

    batch = geo_locator.geocode(name, exactly_one=testing, limit=batch_size, addressdetails=True)
    block = []

    for line in batch:
        item_cat = line.raw['type']
        adress_data = line.raw['address']
        coord_data = (line.raw['lat'],line.raw['lon'])
        #adress_data['name'] = adress_data.pop(item_cat)

        block.append(adress_data)

    frame = pd.DataFrame.from_records(block, index=None)

    return frame



#df = pd.DataFrame.from_records(block,index=None)

result = generate_batch(name='Lowe\'s', batch_size=3)

result.to_csv('output.csv')




