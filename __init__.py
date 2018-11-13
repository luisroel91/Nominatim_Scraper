from geopy.geocoders import Nominatim
import pandas as pd
import time
import numpy as np



biz_names = ['BJs Wholesale Club',
             'Sam\'s club',
             'Costco',
             'Lowe\'s',
             'Home Depot',
             'Menards',
             'Walmart',
             'Target']



master_block = pd.DataFrame([], columns=data_fields)




    for item in batch:
        raw_data = item.raw

        address = raw_data['address']
        item_type = raw_data['type']
        item_name = raw_data['address'][item_type]

        block.append(item_name,address)


        # coordinates = (lst['lat'], lst['lon'])

        # block[]

    # frame = pd.DataFrame(block, columns=data_fields)
    time.sleep(20)

    return block


test_frame = generate_batch(name='Lowe\'s', batch_size=2, testing=False)
print(test_frame)

'''
for biz in biz_names:
    duplicate_counter = 0

    while duplicate_counter < 25:
        data = generate_batch(name=biz,batch_size=10,testing=True)

        if data not in master_block:
'''
