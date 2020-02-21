from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class svmForm(FlaskForm):
    svm_first_field = StringField('Pole 1', validators=[DataRequired()])
    svm_second_field = StringField('Pole 2')
    svm_boolean = BooleanField('Boolean 1')
    svm_submit = SubmitField('Wylicz')
    svm_picker = SelectField(u'Mozliwosci:', choices=[('value1', 'First Value'), ('value2', 'Second Value'), ('value3', 'Third Value')])

class knnForm(FlaskForm):
    knn_first_field = StringField('Pole 1', validators=[DataRequired()])
    knn_second_field = StringField('Pole 2')
    knn_boolean = BooleanField('Boolean 1')
    knn_submit = SubmitField('Wylicz')

class decisionTreeForm(FlaskForm):
    dt_first_field = StringField('Pole 1', validators=[DataRequired()])
    dt_second_field = StringField('Pole 2')
    dt_boolean = BooleanField('Boolean 1')
    dt_submit = SubmitField('Wylicz')

class randomForestForm(FlaskForm):
    rf_first_field = StringField('Pole 1', validators=[DataRequired()])
    rf_second_field = StringField('Pole 2')
    rf_boolean = BooleanField('Boolean 1')
    rf_submit = SubmitField('Wylicz')