import os
import json
import tuyapower
import pandas as pd

FILEPATH = "data.csv"

DEVICES = [
    {
        'plugid': 'bfe05adcc475194032xhir',
        'plugip': '192.168.178.34',
        'plugkey': '86ccc1678b3fd823',
        'plugvers': '3.3',
        'name': '1'
    }
]

def query_consumption(devices):
    data = []

    for device in devices:
        json_output = tuyapower.deviceJSON(
            device['plugid'],
            device['plugip'],
            device['plugkey'],
            device['plugvers']
        )

        parsed_data = json.loads(json_output)
        parsed_data['name'] = device['name']
        data.append(parsed_data)

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
