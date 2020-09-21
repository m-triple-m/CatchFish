from flask import Flask,render_template,request,redirect, flash, jsonify
import os
import random
import whois
import urllib.parse
from urllib.parse import urlparse
from tld import  get_tld
from datetime import datetime
from database import insert_user, getUserByEmail, getAll
from typesquatting import check_typesquatting
from dataset_checker import hasDomain,hasip, check_blacklist, check_legimitate
import random

app=Flask(__name__)
app.secret_key = "###"
    

# ROUTES #########################################

@app.route('/layout')
def layout():
      return render_template('layout.html')
    
@app.route('/')
def home():
      return render_template('home.html',title="CATCHPHISH")
      
@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method=="POST":
        print(request.form)
        user = getUserByEmail(request.form.get('email'))
        if user:
            if user.get('password') == request.form.get('password'):
                print('login success')
                return redirect('/')
            else:
                print('incorrect password')
        else:
            print('user not found!')
        print(getAll())
    return render_template('login.html',title="SIGN IN")
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',title="ADMIN DASHBOARD")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        if len(request.form) > 0 :
            name=request.form.get('name')
            email=request.form.get('email')
            password=request.form.get('password')
            insert_user(name,email,password)
            flash("Entered Successfully")
            return redirect('/login')
            return render_template('process.html',title="CATCHPHISH")
        else:
            flash("Invalid Data")
    return render_template('register.html',title="SIGN UP")

@app.route('/process')
def process():
    return render_template('proces.html',title="CATCHPHISH")

@app.route('/basic',methods=['GET','POST'])
def Basic():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            length_of_url = url_length(url)
            certificate = certificate_checker(url)
            sub_domain = subdomain(url)
            type_squatting = check_typesquatting(url)
            legitimate = check_legimitate(url)
            blacklist = check_blacklist(url)


        return jsonify(length_of_url, certificate, sub_domain, type_squatting, legitimate, blacklist)
    return jsonify('')

@app.route('/enhanced',methods=['GET','POST'])
def Enhanced():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            length_of_url = url_length(url)
            certificate = certificate_checker(url)
            sub_domain = subdomain(url)
            type_squatting = check_typesquatting(url)
            legitimate = check_legimitate(url)
            blacklist = check_blacklist(url)
            registrar_hidden = False
            num_days = True

        return jsonify(length_of_url, certificate, sub_domain, type_squatting, legitimate, blacklist, registrar_hidden, num_days)
    return jsonify('')


@app.route('/result')
def Guage():
    return render_template('gauge.html')
#function call 

#typesquat=check_typesquatting(domain)   #1
#legitimate=hasDomain(domain)         #2
#blacklist=hasip(domain)      #3
#sub_domain=subdomain(url)   #4
#length=url_length(url)      #5

# url details
def domain_details(url):
    try:
        domain=whois.whois(url)
        domain_name=domain.domain_name 
        registration_date=domain.creation_date   #correct it
        registrar_name=domain.registrar
    except Exception as e:
        print(e)
        print('url could not be found')

def url_length(url):
    try:
        length=len(url)      
        if length>10 and length <2038:
            return True
        else:
            return False 
    except:
        return False

def subdomain(url):
    try:
        result = get_tld(url, as_object=True)
        sub_dom=result.subdomain
        category=result
        if sub_dom!="":
            return False
        else:
            return True
    except:
        return False

def certificate_checker(url):
    u=urlparse(url)
    cert=u.scheme
    if cert=='https':
        return True
    else:
        return False



if __name__ == "__main__":
    app.run(debug=True)    

