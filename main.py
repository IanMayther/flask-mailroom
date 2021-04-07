import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = b'\x9d\xb1u\x08%\xe0\xd0p\x9bEL\xf8JC\xa3\xf4J(hAh\xa4\xcdw\x12S*,u\xec\xb8\xb8'
#app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
    '''Redirects to all donations'''
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    '''Displays all donations'''
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     '''Manages donor login'''
#     if request.method == 'POST':
#         donor = Donor.select().where(Donor.name == request.form['name']).get()

#         if donor and pbkdf2_sha256.verify(request.form['password'], donor.password):
#             session['username'] = request.form['name']
#             return redirect(url_for('all_tasks'))

#         return render_template('login.jinja2', error="Incorrect username or password.")

#     else:
#         return render_template('login.jinja2')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    '''Creates donations from a entered user'''
    # if 'username' not in session:
    #     return redirect(url_for('login'))

    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == request.form['name']).get()
        dontation = Donation(donor= request.form['name'], value= request.form['value'])
        print(donor.name, dontation.value)
        dontation.execute()

    return render_template('create.jinja2')

    #     Task.update(performed=datetime.now(), performed_by=user)\
    #         .where(Task.id == request.form['task_id'])\
    #         .execute()

    # return render_template('incomplete.jinja2', tasks=Task.select().where(Task.performed.is_null()))    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

