from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Witaj w mojej aplikacji Flask!"


@app.route('/about')
def about_page():
    return "Zaprogramowano przez Krzysztofa Lisowskiego."


@app.route('/contact')
def contact_page():
    return "Email: kontakt@example.com."


if __name__ == '__main__':
    app.run()
