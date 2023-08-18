from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Cia pradinis puslapis su Flask</h1>'

@app.route('/<kintamasis>')
def user(kintamasis):
    return f'sveiki {kintamasis} atvyke Flask puslapi'

if __name__ == '__main__':
    app.run()

