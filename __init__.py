from func import generate_batch, load_biznames
import pandas as pd
import time
import numpy as np

biz_names = load_biznames()
batch_run = 3

for biz in biz_names:
    repeat_counter = 0
    counter = 0

    while repeat_counter < 25 and counter < batch_run:
        current_batch = generate_batch(name=biz, batch_size=batch_run)
        print(current_batch)



'''

        data_sink = data_sink.join(sink)

        repeats = data_sink.duplicated()
        repeat_counter += repeats.size




# data_sink.to_csv('output.csv')



for biz in biz_names:
    duplicate_counter = 0

    while duplicate_counter < 25:
        data = generate_batch(name=biz,batch_size=10,testing=True)

        if data not in master_block:
'''
