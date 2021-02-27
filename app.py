from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello This is Exam Meet Backend App!"

if __name__ == '__main__':
    app.run(debug=True)