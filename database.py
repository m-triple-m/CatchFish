import pymongo
from pymongo import MongoClient


dbconnection=pymongo.MongoClient("mongodb://localhost:27017/")

db=dbconnection["catchphish_database"]  #creating database

Users=db["Users"]   #creating table

SearchHistory=db["SearchHistory"]

Report=db["Report"]

def insert_user(username,email,password):
    try:   
        insert={ 
                 uname:username,
                 email:email,
                 password:password                        
                }
        x=Users.insert_one(insert)
    except:
        print("Some error has occured")

def insert_search_history(search_url,user_id,date):
    try:
        history={
                    url:search_url,
                    id:user_id,
                    search_date:date
        }
    except:
        print("Some error has occured")
        
def insert_report(pub_date,search_id,url_id,report_name):
    try:
        report={
                    date:pub_date,
                    s_id:search_id,
                    url-id:url_id,
                    report_name:report_name
        }
    except:
        print("Some error has occured")












                                                                                                  