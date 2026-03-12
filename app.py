import os
from flask import Flask

app = Flask(__name__)

# FIX: Get the password from the system environment, not the code
DB_PASSWORD = os.environ.get("DB_PASSWORD", "default_safe_value") 

@app.route("/")
def home():
    return "Product Security Pipeline is SECURE!"

if __name__ == "__main__":
    # FIX: Set debug to False for production
    app.run(debug=False) 

