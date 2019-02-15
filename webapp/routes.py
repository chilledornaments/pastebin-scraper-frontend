from webapp import app
from webapp.backend import mongo_loader
from flask import render_template, request, send_from_directory, flash, redirect, url_for
from werkzeug.urls import url_parse
import json, os

@app.route('/')
def homepage():
    # Need to give link to view alerts of different statuses
    return render_template('homepage.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/all')
def all_alarms():
    docs = mongo_loader.loader("All")
    return render_template('status_all.html', data=docs)

@app.route('/unclassified')
def unsure_alarms():
    docs = mongo_loader.loader("Maybe")
    return render_template('maybe.html', data=docs)

@app.route('/false_alarms')
def false_alarms():
    docs = mongo_loader.loader("Miss")
    return render_template('miss.html', data=docs)

@app.route('/confirmed_alarms')
def confirmed_alarms():
    docs = mongo_loader.loader("Match")
    return render_template('match.html', data=docs)

@app.route('/update/<id>/<status>')
def update_record(id, status):
    docs = mongo_loader.updater(id, status)
    flash(docs)
    return redirect(request.referrer)