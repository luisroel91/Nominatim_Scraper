from func import generate_batch, load_biznames
import pandas as pd
import time
import numpy as np

biz_names = load_biznames()
batch_run = 3

for biz in biz_names:
    repeat_counter = 0
    data_sink = pd.DataFrame()

    while repeat_counter < 25:
        current_df = generate_batch(name=biz, batch_size=batch_run)

        data_sink.join(current_df)








'''
for biz in biz_names:
    duplicate_counter = 0

    while duplicate_counter < 25:
        data = generate_batch(name=biz,batch_size=10,testing=True)

        if data not in master_block:
'''
