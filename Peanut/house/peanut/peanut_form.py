from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,DateTimeField,TextAreaField
from wtforms.validators import DataRequired



class MyFrom(FlaskForm):      #表单的样子
    title = StringField('Title',validators=[DataRequired()])
