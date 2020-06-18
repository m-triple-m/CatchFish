from flask import Flask,render_template,request,redirect
import os
import random
import whois
import urllib.parse
from urllib.parse import urlparse
from tld import  get_tld
from datetime import datetime
from database import insert_user
from typesquatting import check_typesquatting
from dataset_checker import hasDomain,hasip

app=Flask(__name__)
    

# ROUTES #########################################

@app.route('/layout')
def layout():
      return render_template('layout.html')
    
@app.route('/')
def home():
      return render_template('home.html',title="CATCHPHISH")
      
@app.route('/login')
def login():
      return render_template('login.html',title="SIGN IN")
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',title="ADMIN DASHBOARD")

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html',title="SIGN UP")
    if request.method=='POST':
        if len(name) > 0 :
            name=request.form.get('name')
            email=request.form.get('email')
            password=request.form.get('password')
            insert_user(name,email,password)
            flash("Entered Successfully")
            return redirect()
            return render_template('process.html',title="CATCHPHISH")
        else:
            flash("Invalid Data")
            return render_template('register.html',title="SIGN UP")

@app.route('/process',methods=['GET','POST'])
def process():
    return render_template('process.html',title="CATCHPHISH")

#function call 

#typesquat=check_typesquatting(domain)   #1
#legitimate=hasDomain(domain)         #2
#blacklist=hasip(domain)      #3
#sub_domain=subdomain(url)   #4
#length=url_length(url)      #5

# url details
def domain_details(url):
    domain=whois.whois(url)
    domain_name=domain.domain_name 
    registration_date=domain.creation_date   #correct it
    registrar_name=domain.registrar

def url_length(url):
    try:
        length=len(url)      
        if length>10 and length <2038:
            return random.randrange(80,98)
        else:
            return random.randrange(50,60) 
    except:
        return random.randrange(30,60)

def subdomain(url):
    try:
        result = get_tld(url, as_object=True)
        sub_dom=result.subdomain
        category=result
        if sub_dom!="":
            return random.randrange(80,96)
        else:
            return random.randrange(60,80)
    except:
        return random.randrange(30,50)

def certificate_checker(url):
    u=urlparse(url)
    cert=u.scheme
    if cert=='https':
        return 100
    else:
        return random.randrange(50,81)



if __name__ == "__main__":
    app.run(debug=True)    

