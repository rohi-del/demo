from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Rohit 🚀 Your GitHub Actions deployment is working on EC2!"

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
