from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from website.string_support import *
from website.models import User
from . import db, login_manager

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login_data = request.form
        for field, value in login_data.items():
            if not value:
                flash('Please fill all fields before submitting.', category='err')
                return render_template('login.html')

        email = login_data.get('email')
        password = login_data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and hash_string(password) == user.hashed_password:
            # Login successful
            login_user(user)
            flash('Login successful!', category='success')
            return redirect(url_for('views.homepage'))
        else:
            # Login failed
            flash('Invalid email or password. Please try again.', category='err')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        sign_up_data = request.form
        for field, value in sign_up_data.items():
            print(value)
            if not value:
                flash('Please fill all fields before submitting.', category='err')
                return render_template('sign-up.html')
        email = sign_up_data.get('email')
        username = sign_up_data.get('username')
        first_name = sign_up_data.get('first_name')
        last_name = sign_up_data.get('last_name')
        age = sign_up_data.get('age')
        password = sign_up_data.get('password')
        password_confirm = sign_up_data.get('password_confirm')
        print(password, password_confirm)
        valid = True
        if password_confirm != password:
            flash('Submitted passwords do not match.', category='err')
            valid = False
        if len(password) < 8:
            flash('Password needs to be at least 8 characters.', category='err')
            valid = False
        if not has_lowercase(to_check=password):
            flash('Password needs to have at least one lowercase letter.', category='err')
            valid = False
        if not has_uppercase(to_check=password):
            flash('Password needs to have at least one uppercase letter.', category='err')
            valid = False
        if not has_special_characters(to_check=password):
            flash('Password needs to have at least one special character.', category='err')
            valid = False
        if not has_numbers(to_check=password):
            flash('Password needs to have at least one number', category='err')
            valid = False
        if int(age) <= 0:
            flash('Age must be a positive number', category='err')
            valid = False
        if User.query.filter_by(email=email).first():
            flash('Account already exists with the given email.', category='err')
            valid = False
        
        if valid:
            new_user = User(email=email, username=username, hashed_password=hash_string(password), \
                            age=age, first_name=first_name, last_name=last_name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

    return render_template('sign-up.html')