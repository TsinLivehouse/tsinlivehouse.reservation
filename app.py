from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Club Reservation v3 (Render Ready) - Customer Form"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
