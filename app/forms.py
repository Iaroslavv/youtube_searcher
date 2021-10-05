from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired

class SearhForm(FlaskForm):
    myChoices = ['Views', 'Rating', 'Likes', 'Duration'] # need to fix
    video_name = StringField("Video name", validators=[DataRequired()])
    videos_number = IntegerField("Amount of videos", validators=[DataRequired()])
    comments_number = IntegerField("Amount of comments", validators=[DataRequired()])
    filter_by = SelectField(u'Filter By', choices = myChoices)
    submit = SubmitField("Apply")
