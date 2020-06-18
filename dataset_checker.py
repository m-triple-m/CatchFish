import pandas as pd
import socket

def check_legimitate(domain_name):
    data1=pd.read_csv("C:/Users/PRIYANSHI/Documents/python/phishing and pharming/database/datasets/domain.csv")
    hasDomain(data,domain_name) #return true or false

def hasDomain(dataset,domain,col='Domain'):
    return bool(dataset[dataset[col].str.contains(domain)].shape[0])


def check_blacklist(domain_name):
    ip=socket.gethostbyname(domain_name)
    data=pd.read_csv("C:/Users/PRIYANSHI/Documents/python/phishing and pharming/database/datasets/blacklist_ip.csv",
            names=["ip_address","abc","klj","hjhgjh"])
    value=hasip(data,ip)  #hasip is a function name
    return value


def hasip(dataset,domain,col='ip_address'):
    return bool(dataset[dataset[col].str.contains(domain)].shape[0])
    

