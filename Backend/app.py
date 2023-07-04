from flask import Flask
from flask_cors import CORS,cross_origin


UPLOAD_FOLDER = r'I:\Dan dev\NHCE\Mini Project\Image Captioning\Backend'

app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024