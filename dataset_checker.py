import pandas as pd
import socket

def check_legimitate(domain_name):
    data=pd.read_csv("database/datasets/domain.csv")
    return hasDomain(data,domain_name) #return true or false

def hasDomain(dataset,domain,col='Domain'):
    return bool(dataset[dataset[col].str.contains(domain)].shape[0])


def check_blacklist(domain_name):
    try:
        ip=socket.gethostbyname(domain_name)
        data=pd.read_csv("database/datasets/blacklist_ip.csv",
                names=["ip_address","abc","klj","hjhgjh"])
        value=hasip(data,ip)  #hasip is a function name
        return value
    except Exception as e:
        print(e)
        return None


def hasip(dataset,domain,col='ip_address'):
    return bool(dataset[dataset[col].str.contains(domain)].shape[0])
    

