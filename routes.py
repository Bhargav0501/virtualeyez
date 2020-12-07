import base64

from app import app
from flask import render_template, redirect, url_for, request, flash, jsonify
from forms import UploadForm
from virtualeyez import Reader
import io
from PIL import Image, ImageDraw
import numpy as np
from textblob import TextBlob


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
        lang = 'en'
        if 12.41 <= float(lat) <= 19.07 and 77 <= float(lon) <= 84.40:
            lang = 'te'
        elif 8.5 <= float(lat) <= 13.35 and 76.15 <= float(lon) <= 80.20:
            lang = 'ta'
        elif 11.3 <= float(lat) <= 18.3 and 74 <= float(lon) <= 78.3:
            lang = 'ka'
        image = Image.open(io.BytesIO(var))
        img = np.array(image)
        reader = Reader(['en', 'hi'])
        bounds = reader.readtext(img)
        if lang != 'en':
            reader1 = Reader([lang])
            bounds1 = reader1.readtext(img)
            for i in range(len(bounds)):
                bounds[i] = list(bounds[i])
                bounds[i][1] = (bounds1[i][1] + ' - ' + TextBlob(bounds1[i][1]).detect_language()
                                if bounds[i][2] < bounds1[i][2]
                                else bounds[i][1] + ' - ' + TextBlob(bounds[i][1]).detect_language())
        image_with_bounds = draw_boxes(image, bounds)
        buffered = io.BytesIO()
        image_with_bounds.save(buffered, format="png")
        b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        text = "\n".join([i[1] for i in bounds])
        return render_template('result.html', image="data:image/png;base64," + b64, text=text, lat=lat, lon=lon)
    return render_template('index.html', form=form)
