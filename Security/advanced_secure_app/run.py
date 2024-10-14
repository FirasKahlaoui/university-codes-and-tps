from app import create_app
from flask import redirect, url_for, render_template
from app.forms import LoginForm

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('main.login'))


if __name__ == '__main__':
    app.run(debug=True)
