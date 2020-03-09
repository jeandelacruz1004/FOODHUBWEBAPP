from web import Flask, render_template, request, url_for, redirect,flash, server, session
from flask_login import logout_user
import requests
from datetime import timedelta

#Routing for landing pages

@server.route("/", methods=['GET', 'POST'])
@server.route('/')
def home():
    return render_template('landing.html')