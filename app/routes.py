from flask import render_template, redirect, url_for, request
from app import app
from app.forms import SearhForm
from app.parsers.video_parse import YoutubeSearcher

@app.route('/', methods=['POST', 'GET'])
def main_page():
    form = SearhForm()
    if form.validate_on_submit():
        video_name = str(request.form['video_name'])
        videos_number = int(request.form['videos_number'])
        number_of_commments = int(request.form['comments_number'])
    searcher = YoutubeSearcher(video_name=video_name, videos_number=videos_number, comments_number=number_of_commments) \
                .filter_results()
    print(searcher)
    return render_template('layout.html', form=form)


