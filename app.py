from flask import Flask, render_template
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie

app = Flask(__name__)

HTML_TEMPLATE = "index.html"
@app.route("/")
def main():
    return render_template(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
