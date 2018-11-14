from func import generate_batch, load_biznames
import pandas as pd
import time
import numpy as np

biz_names = load_biznames()
batch_run = 3

counter = 0

while counter < batch_run:

    data_sink = pd.DataFrame()

    for biz in biz_names:
        current_batch = generate_batch(name=biz, batch_size=batch_run)
        data_sink = pd.concat([data_sink, current_batch], ignore_index=True)

        counter += 1
        # repeat_counter = sink.duplicated().size


    data_sink.to_csv('output.csv')
