#test app
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '7cd18ff261d5dbe21f54af94fb3a78cc'

posts = [
    {
        'author':'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted':'April 26, 2019'
    },
    {
        'author':'Jane Smith',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted':'April 27, 2019'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form =RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form =LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
        app.run(debug=True)

