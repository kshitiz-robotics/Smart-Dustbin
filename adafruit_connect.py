from Adafruit_IO import Client
import Config
from time import sleep
import databse_connect

ADAFRUIT_IO_KEY = Config.ADAFRUIT_IO_KEY
ADAFRUIT_IO_USERNAME = Config.ADAFRUIT_IO_USERNAME
FEED_ID =databse_connect.get_feed_id()
print(FEED_ID)
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


# Connect to the Adafruit IO server.
def get_data(FEED_ID,delay):
    data_dict={}
    try:
        for i in FEED_ID:
            sleep(delay)
            data = aio.receive(i)
            value = ('{0}'.format(data.value))
            data_dict[i]=value
        return data_dict
    except:
        return 501
print(get_data(FEED_ID,2))