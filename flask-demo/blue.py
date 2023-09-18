from flask import Blueprint, request, render_template, g, make_response, redirect, url_for, session
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

a = Blueprint('a', __name__)


@a.route('/aaa', methods=['GET', 'POST'])
def index():
    print('aaaabbb')
    return render_template('index.html', name=session.get('name'))

