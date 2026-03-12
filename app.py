import os
from flask import Flask

app = Flask(__name__)

# SECURITY ISSUE: A hardcoded secret (Bandit will hate this)
DB_PASSWORD = "super_secret_password123" 

@app.route("/")
def home():
    return "Product Security Pipeline is Running!"

if __name__ == "__main__":
    app.run(debug=True)
