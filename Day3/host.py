from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="7070")

#* Serving Flask app "main" (lazy loading)
#* Environment: production
# WARNING: Do not use the development server in a production environment.
#   Use a production WSGI server instead.
# * Debug mode: off
# * Running on http://127.0.0.1:7070/ (Press CTRL+C to quit)
