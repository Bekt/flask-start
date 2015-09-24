import wtforms as wt

from ..wrappers import Form


class SignupForm(Form):
    name = wt.StringField('Name', [wt.validators.Length(min=2, max=70)])
    email = wt.StringField('Email', [wt.validators.Email()])
    password = wt.StringField('Password', [wt.validators.Length(min=6, max=70)])
