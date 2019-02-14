from webapp import app
from webapp.backend import mongo_loader
from flask import render_template, request, send_from_directory
import json, os

@app.route('/')
def homepage():
    # Need to give link to view alerts of different statuses
    return render_template('homepage.html')

@app.route('/all')
def all_alarms():
    docs = mongo_loader.loader("All")
    return "Hello world"

@app.route('/inactioned')
def unsure_alarms():
    docs = mongo_loader.loader("Maybe")
    return "hello world"

@app.route('/false_alarms')
def false_alarms():
    docs = mongo_loader.loader("False")
    return "hello world"

@app.route('/confirmed_alarms')
def confirmed_alarms():
    docs = mongo_loader.loader("True")
    return "hello world"

@app.route('/update_record')
def update_record(id, status):
    docs = mongo_loader.updater(id, status)
    return render_template('updating.html')