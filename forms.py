from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField, StringField


class UploadForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'webp', 'jfif'], 'Images only!')
    ])
    latitude = StringField()
    longitude = StringField()
    submit = SubmitField()
