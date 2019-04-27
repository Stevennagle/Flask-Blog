#test app
from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
        app.run(debug=True)

