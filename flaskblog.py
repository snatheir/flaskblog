from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e1953e4286de87ce049e87e26fc85386'

posts = [
    {
        'author': 'Sharif Natheir',
        'title': 'My first post',
        'content': 'My first posts content',
        'date_posted': 'June 5, 2020'
    },
    {
        'author': 'Mustafa Natheir',
        'title': 'My second post',
        'content': 'My first posts content',
        'date_posted': 'June 25, 2020'
    }
]






@app.route("/")
def hello():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)