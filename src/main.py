from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><head><title>My Web Server</title></head><body><p>This is an example web server.</p></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
