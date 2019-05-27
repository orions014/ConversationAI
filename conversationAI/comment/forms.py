__author__ = 'Mitu'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,BooleanField,RadioField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from markupsafe import Markup


class CommentPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later

    comment = TextAreaField('Post a Comment', validators=[DataRequired()])

    submit = SubmitField('Post')