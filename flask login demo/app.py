from flask import Flask,render_template,request,flash,url_for,redirect
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required
from flask_migrate import Migrate


basedir=os.path.dirname(os.path.realpath(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='7b7f78b8ce2f66825112a658'


db=SQLAlchemy(app)
login_manager=LoginManager(app)

login_manager.login_view='login'




class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password_hash=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return f" User <{self.username}>"


@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))

@app.route('/')
def index():
    user=User.query.filter_by(username)
    return render_template('index.html',user=user)


@app.route('/login',methods=['GET','POST'])
def login():

    username=request.form.get('username')
    password=request.form.get('password')

    user=User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash,password):
        login_user(user)

        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def register():

    if request.method == 'POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm=request.form.get('confirm')

        user=User.query.filter_by(username=username).first()

        if user:
            flash(f"User with username {username} exists")
            return redirect(url_for('register'))

        email_exists=User.query.filter_by(email=email).first()

        if email_exists:
            flash(f"User with email {email} exists")
            return redirect(url_for('register'))


        password_hash=generate_password_hash(password)

        new_user=User(username=username,
            email=email,
            password_hash=password_hash)

        db.session.add(new_user)
        db.session.commit()

        flash("User account created")

        return redirect(url_for('login'))    


    return render_template('signup.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html')

@app.errorhandler(500)
def server_error(error):
    return render_template('server_error.html')


if __name__ == "__main__":
    app.run(debug=False)