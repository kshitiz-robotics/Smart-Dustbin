import adafruit_connector
import databse_connect
import fastsms_alert
from time import sleep
import Config

if __name__ == '__main__':
    print(" -----------------------------------")
    print("|  Smart Dustbin Alert Application  |")
    print(" -----------------------------------")
    """"""
    print(" ````````Command Shortcut``````````` ")
    print(" ____________________________________")
    print("|     START     |          1         |")
    print("|     STOP      |          0         |")
    print("|     PAUSE     |          8         |")
    print(" ____________________________________")


    s=int(input("Enter Command : "))
    if s==1:
        print("Initlizing Alert System ....")
        print("Please wait till Loading Configuration and dependencies..")
    elif s==0:
        exit()
    else:
        print("Not a valid Command ")
        print("exiting program ....")
        exit()

    # getting feed id from database
    while True:
        feedid= databse_connect.get_feed_id()

        print("----------Getting Feeds ID from Databse------------ ")
        for i in feedid:
            sleep(0.5)
            print(f"Feeds ID --> {i}")
        print("")

        # Getting data from the Adafruit IO Server
        bin_data = adafruit_connector.get_data(feedid,Config.delay)

        print("")
        print("---------Sorting Data for Full dustbins------------ ")
        print(f"           Condition : Full if >{Config.cutoff_percentage} % ")


        full_bin = adafruit_connector.list_of_full_bins(bin_data,Config.cutoff_percentage)

        print("---------Initilizing alert to Workers-------------- ")
        for items in full_bin:
            all_details =databse_connect.get_all_details(items)
            worker_name=all_details[1]
            contact_no=all_details[2]
            #creaating message
            message = fastsms_alert.generate_sms(worker_name,items,full_bin[items])
            #sending message
            responce = fastsms_alert.send_sms(contact_no,message)
            print(responce)
            print(f"Alerted !!!! ")
            print(f"Sucessfully to {worker_name} on his Contact NO {contact_no} ")

        print("All alerts has been sended !!!!!!! ")
        s = input("Any key to continue for exit press 0")

        if int(s)==0:
            exit()


1