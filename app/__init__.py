from flask import Flask
import logging

with open("image_list.txt", "r") as f:
    image_urls = f.read().splitlines()

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

from . import views
