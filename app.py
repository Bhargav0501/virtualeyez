# from virtualeyez.virtualeyez import Reader
#
# reader = Reader(['en'])
# result = reader.readtext('noisy-image.jpg')
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

import routes

if __name__ == '__main__':
    app.run(port=5500)
