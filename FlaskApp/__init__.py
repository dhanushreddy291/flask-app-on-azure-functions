from flask import Flask

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)

@app.route('/')
def index():
    return "A Web App with Python (Flask) on Microsoft Azure Functions!"

if __name__ == "__main__":
    app.run()