import sys
from Adafruit_IO import Client
import Config
import main
from time import sleep
ADAFRUIT_IO_KEY = Config.ADAFRUIT_IO_KEY
ADAFRUIT_IO_USERNAME = Config.ADAFRUIT_IO_USERNAME


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Connect to the Adafruit IO server.
def get_data(FEED_ID,delay):
    data_dict={}
    print("----------Getting Smart Dustbin Details----------- ")
    try:
        for i in FEED_ID:
            sleep(delay)
            data = aio.receive(i)
            value = ('{0}'.format(data.value))
            data_dict[i]=value
            print(f"Bin ID : {i} filled {value} % of total capacity.")
        return data_dict
    except:
        return 501
def list_of_full_bins(bindata,cutoff_percentge):
    full_bin = {}
    for key in bindata.keys():
        value=bindata.get(key)
        if int(value) > cutoff_percentge :
            full_bin[key]=value
            sleep(0.3)
            print(f"Bin ID : {key}  Full !! ")

    return full_bin
