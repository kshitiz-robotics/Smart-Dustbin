import adafruit_io
FEED_ID = ['sd01', 'sd02', 'sd03', 'sd04', 'sd05']
def list_of_full_bins(bindata,cutoff_percentge):
    full_bin = {}
    for key in bindata.keys():
        value=bindata.get(key)
        if int(value) > cutoff_percentge :
           full_bin[key]=value


    print(full_bin)
if __name__ == '__main__':
    bin_data=adafruit_io.get_data(FEED_ID,1)
    list_of_full_bins(bin_data,70)
