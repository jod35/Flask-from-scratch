from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,SubmitField
from wtforms.validators import InputRequired,EqualTo,Length
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(BASE_DIR,'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)




app.secret_key='ojdwindiowndowniodn'


class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(25),nullable=False)
    content=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return self.title

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(25),nullable=False,unique=True)
    email=db.Column(db.String(40),nullable=False,unique=True)
    password_hash=db.Column(db.Text())

    def __repr__(self):
        return self.username



class SignUpForm(FlaskForm):
    username=StringField(label="Username",validators=[InputRequired(message="Username should not be blank"),
    Length(min=5,max=25)])

    email=StringField(label="Email",validators=[InputRequired(message="Email should not be blank"),Length(max=45,
    message="Email should have less than 45 characters"
    )])

    password=PasswordField(label="Password",validators=[InputRequired(message="Password should not be left blank"),
        Length(min=5,max=12,message="Password should be between 5 and 12 characters")
    ])

    confirm=PasswordField(label="Confirm Password",validators=[InputRequired(message="Password should not be left blank"),
        Length(min=5,max=12,message="Password should be between 5 and 12 characters"),EqualTo('password',message="Passwords do not match")
    ])

    submit=SubmitField(label="Sign Up")


class LoginForm(FlaskForm):
    email=StringField(label="Email",validators=[InputRequired(message="Email should not be blank"),Length(max=45,
    message="Email should have less than 45 characters"
    )])
    password=PasswordField(label="Password",validators=[InputRequired(message="Password should not be left blank"),
        Length(min=5,max=12,message="Password should be between 5 and 12 characters")
    ])
    submit=SubmitField(label="Login")

    

@app.route('/')
def index():

    title="Home page"
    
    context={
        'title':title,
        'posts':posts
    }
    return render_template('index.html',**context)

@app.route('/about')
def about_page():
    title="About page"
    context={
        'title':title
    }
    return render_template('about.html',**context)

@app.route('/login')
def login_page():
    title="Login page"
    form=LoginForm()
    context={
        'title':title,
        'form':form
    }
    return render_template('login.html',**context)

@app.route('/signup',methods=["GET","POST"])
def signup():
    form=SignUpForm()

    if request.method == "POST":
        if form.validate_on_submit():
            return "Validation worked"


    context={
        'form':form
    }
    return render_template('signup.html',**context)


@app.route('/contacts')
def contacts_page():
    title="Contacts page"
    context={
        'title':title
    }
    return render_template('contacts.html',**context)

@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'User':User,
        'Post':Post
    }

if __name__ == "__main__":
    app.run(debug=True)