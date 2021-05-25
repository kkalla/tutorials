from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return_html = '''<!DOCTYPE HTML><html>
        <head></head>
        <body><h1>Hello World</h1></body>
    </html>'''
    return return_html


if __name__ == "__main__":
    app.run(port=7000, debug=True)