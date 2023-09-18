from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
class NameForm(Form):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')
from blue import a
app.register_blueprint(a)
from flask import Flask, render_template, session, redirect, url_for
@app.route('/aaaaaa', methods=['GET', 'POST'])
def index():
    print('aaaa')
    form = NameForm()
    if form.validate():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
	app.run(debug=True)