import pymysql
import Config
# enter your server IP address/domain name
HOST = Config.HOST # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = Config.DATABASE
# this is the user you create
USER = Config.USER
# user password
PASSWORD = Config.PASSWORD
# connect to MySQL server
db= pymysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db.get_server_info())
# enter your code here!
mycursor = db.cursor()

# mycursor.execute("SELECT bin_id FROM bin ")
# # mycursor.execute("SELECT * FROM bin WHERE bin_id ='sm05'")
# res=mycursor.fetchall()

def get_feed_id():
    mycursor.execute("SELECT bin_id FROM bin ")
    list_of_feed = mycursor.fetchall()
    from itertools import chain
    list_of_feed=(list(chain(*list_of_feed)))
    return list_of_feed

def get_all_details(binid):
    mycursor.execute(f"SELECT * FROM bin WHERE bin_id ='{binid}'")
    res = mycursor.fetchone()
    binid=res[0]
    name=res[1]
    contact_no=res[2]
    return [binid,name,contact_no]


if __name__ == '__main__':
    # mycursor.execute("SELECT bin_id FROM bin ")
    # mycursor.execute("SELECT * FROM bin WHERE bin_id ='sd05'")
    # res=mycursor.fetchall()
    # print(res)
    # print(type(res))
    res= get_all_details('sd01')

    print(type(res))
    print(res)