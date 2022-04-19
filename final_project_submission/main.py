from flask import Flask
from data_checkpoint import app_data

main_app = Flask(__name__)
main_app.register_blueprint(app_data)


main_app.run(debug=True, port=8000)