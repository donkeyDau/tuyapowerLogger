import os
import json
import pandas as pd


FILEPATH = "data.csv"


DEVICES = [
    {
        'plugid': '',
        'plugip': '',
        'plugkey': '',
        'plugvers': '',
    },
]


def query_consumption(devices):
    data = []

    for device in devices:
        json_output = tuyapower.json_str(
            device['plugid'],
            device['plugip'],
            device['plugkey'],
            device['plugvers']
        )

        data.append(json.reads(json_output))

    return data


def write_data_to_csv(filepath, data_dict_list):
    dataframes = [pd.DataFrame(dict_, index=[idx]) 
        for idx, dict_ in enumerate(data_dict_list)]

    df = pd.concat(dataframes)

    if os.path.isfile(filepath):
        df.to_csv(filepath, mode='a', index=False, header=False)
    else:
        df.to_csv(filepath, index=False)

def main():
    data = query_consumption(DEVICES)

    write_data_to_csv(FILEPATH, data)


if __name__ == '__main__':
    main()
