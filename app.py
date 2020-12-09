# from virtualeyez.virtualeyez import Reader
#
# reader = Reader(['en'])
# result = reader.readtext('noisy-image.jpg')
from flask import Flask
from config import Config
import logging
app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.INFO)
import routes

if __name__ == '__main__':
    app.run(debug=True)
