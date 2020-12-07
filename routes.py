import base64

from app import app
from flask import render_template, redirect, url_for, request, flash, jsonify
from forms import UploadForm
from virtualeyez import Reader
import io
from PIL import Image, ImageDraw
import numpy as np


def draw_boxes(image, bounds, color='red', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


@app.route('/', methods=['get', 'post'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        var = form.image.data.stream.read()
        lat = form.latitude.data
        lon = form.longitude.data
        image = Image.open(io.BytesIO(var))
        img = np.array(image)
        reader = Reader(['en', 'hi'])
        bounds = reader.readtext(img)
        image_with_bounds = draw_boxes(image, bounds)
        buffered = io.BytesIO()
        image_with_bounds.save(buffered, format="png")
        b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        text = "\n".join([i[1] for i in bounds])
        return render_template('result.html', image="data:image/png;base64," + b64, text=text, lat=lat, lon=lon)
    return render_template('index.html', form=form)
