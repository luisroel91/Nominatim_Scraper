from geopy.geocoders import Nominatim
from get_batch import generate_batch
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

result = generate_batch(name='Lowe\'s', batch_size=10)

result.to_csv('output.csv')


'''
for biz in biz_names:
    duplicate_counter = 0

    while duplicate_counter < 25:
        data = generate_batch(name=biz,batch_size=10,testing=True)

        if data not in master_block:
'''
