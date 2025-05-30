from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.critical import bp as critical_bp
app.register_blueprint(critical_bp)

if __name__ == "__main__":
    app.run(debug=True)