import pandas as pd
import json
import os


class Price():

    def getData(slice=0):
        if not os.path.exists('../data/rec/rec.json'):
            if os.path.exists('../data/rec/rec.csv'):
                csv_data = pd.read_csv('../data/rec/rec.csv')
                csv_data.to_json('rec.json', orient='records',
                                 force_ascii=False)
        if os.path.exists('../data/rec/rec.json'):
            with open('../data/rec/rec.json', encoding="utf-8-sig") as json_data:
                dict_data = json.load(json_data)
                if slice == 0:
                    return dict_data
                else:
                    return dict_data[:slice]
        else:
            print("File not exist")
            return None
