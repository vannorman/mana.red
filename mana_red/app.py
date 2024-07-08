import os
import sys
from datetime import datetime
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, jsonify, request

try: from settings_local import mail
except: pass

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# import logging
#app.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG for debugging
# logging.basicConfig(filename='/home/ubuntu/mana.red/mana_red/flask.log', level=logging.DEBUG)

@app.route('/waitlist/apply', methods=['POST'])
def waitlist_apply():
    data = request.get_json()
    ip = request.remote_addr
    to = ['charlie@vannorman.ai' ]
    fr = 'charlie@mana.red'
    subject = "Mana Games - Waitlist";
    text = str(data);
    text += " ip : "+str(ip)
    server = 'mana.red'
    #mail.sendMail(to, fr, subject, text,server)

    path = "static/lists/"
    now = datetime.now()
    today = now.strftime("%Y.%m.%d")
    if not os.path.exists(path):
        os.makedirs(path)
    filename = os.path.join(path,"mailing_list.csv")
    if not os.path.exists(filename):
        with open(filename,'w+'):
            pass

    try:
        
        with open (filename, "a") as file:
            file.write(",".join([ip,str(data),today])+"\n")
        return jsonify({'success':True});
    

    except: 
        return jsonify({'success':False})            




@app.route('/analytics')
def analytics():
    return render_template('analytics.html',)

@app.route('/waitlist')
def waitlist():
    return render_template('waitlist.html',)

@app.route('/internship')
def internship():
    return render_template('internship.html',)

@app.route('/')
def home():
    return render_template('index.html',)

if __name__ == '__main__':
    app.run()

