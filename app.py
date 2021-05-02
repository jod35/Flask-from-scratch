from flask import Flask,render_template

app=Flask(__name__)


posts=[
    {
        'id':1,
        'title':'What a good day',
        'content':'To go swimming at the beach'
    },
       {
        'id':2,
        'title':'Python is fun',
        'content':'I am learning it'
    },
       {
        'id':3,
        'title':'Coding is hard',
        'content':'So learn it better'
    },
       {
        'id':4,
        'title':'I love Python',
        'content':'It is easy'
    },
]


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
    context={
        'title':title
    }
    return render_template('login.html',**context)

#adding params to urls

# @app.route('/greet/<user>')
# def greet(user):
#     return f"Hello {user}"

# @app.route('/greet/<string:user>/<int:age>')
# def greet_user(user,age):
#     return f"This is {user} and you are {age}"

@app.route('/contacts')
def contacts_page():
    title="Contacts page"
    context={
        'title':title
    }
    return render_template('contacts.html',**context)


if __name__ == "__main__":
    app.run(debug=True)