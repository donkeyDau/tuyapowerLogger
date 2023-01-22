# tuyapowerLogger

Basic logging functionality for creating a timestamped based history of power consumption and so forth in a CSV file.

## Installation

Create a python virtual environment with `python -m venv .env` which creates the virtual environment in the folder .env.

Activate python virtual environment with `.\.env\Scripts\activate` using Windows or `source .env/bin/activate` on Linux.

Install required packages with `pip install -r requirements.txt`.

## Parametrize

All information about devices need to be added at the top of the script in list of dictionaries named `DEVICES`. Format looks like:

```
DEVICES = [
    {
        'plugid': '01234567891234567890',
        'plugip': '10.0.1.99',
        'plugkey': '0123456789abcdef',
        'plugvers': '3.3',
    },
]
```

Details about keys see [tuyapower pacakge](https://github.com/jasonacox/tuyapower).

Data will be stored at path defined in variable `FILEPATH`.

## Run script

For running the script one needs to activate the python virtual environment as described in _Installation_. And call `python log_consumption.csv`.
