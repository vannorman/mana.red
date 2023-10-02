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

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# import logging
#app.logger.setLevel(logging.DEBUG)  # Set log level to DEBUG for debugging
# logging.basicConfig(filename='/home/ubuntu/mana.red/mana_red/flask.log', level=logging.DEBUG)

@app.route('/internship/apply', methods=['POST'])
def internship_apply():
    data = request.get_json()
#    app[data]
    to = ['charlie@vannorman.ai','federico.chialvo@gmail.com']
    fr = 'charlie@mana.red'
    subject = "Internship Application Received";
    text = str(data);
    server = 'mana.red'
    mail.sendMail(to, fr, subject, text,server)
#     mail.sendMail(['charlie@vannorman.ai'],'charlie@mana.red','test2','test3','mana.red')
    return jsonify({'success':True});

@app.route('/analytics')
def analytics():
    return render_template('analytics.html',)

@app.route('/internship')
def internship():
    return render_template('internship.html',)

@app.route('/')
def home():
    return render_template('index.html',)

if __name__ == '__main__':
    app.run()

