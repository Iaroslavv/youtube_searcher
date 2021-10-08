from flask import render_template, redirect, url_for
from app import app
from app.forms import SearhForm
from app.parsers.video_parse import YoutubeSearcher


@app.route('/', methods=['POST', 'GET'])
def main_page():
    form = SearhForm()
    if form.validate_on_submit():
        video_name = form.video_name.data
        videos_number = form.videos_number.data
        number_of_commments = form.comments_number.data
        filter_by = form.filter_by.data
        YoutubeSearcher(video_name=video_name, videos_number=videos_number,
                        comments_number=number_of_commments, search_by=filter_by).filter_results()
        return redirect(url_for('results'))
    return render_template('layout.html', form=form)

@app.route('/results', methods=['POST', 'GET'])
def results():
    return render_template('results.html')