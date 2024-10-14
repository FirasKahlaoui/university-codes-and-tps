from app import create_app
from flask import Flask, redirect, url_for

app = Flask(__name__, static_folder='app/static')
app = create_app(app)


@app.route('/')
def index():
    return redirect(url_for('main.login'))


if __name__ == '__main__':
    app.run(debug=True)
