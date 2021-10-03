from flask import render_template, redirect, url_for
from app import app


@app.route('/', methods=['POST', 'GET'])
def main_page():
    return 'Hello world'


