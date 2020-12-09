import base64

from app import app
from flask import render_template, redirect, url_for, request, flash, jsonify
from forms import UploadForm
from virtualeyez import Reader
import io
from PIL import Image, ImageDraw
import numpy as np
from textblob import TextBlob
from translate import Translator


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
        temp = []
        if lang != 'en':
            reader1 = Reader([lang])
            bounds1 = reader1.readtext(img)
            for i in range(len(bounds)):
                bounds[i] = list(bounds[i])
                bounds[i][1] = (bounds1[i][1]
                                if bounds[i][2] < bounds1[i][2]
                                else bounds[i][1])
                tem = False
                for x in bounds[i][1]:
                    if ord(x) > 255:
                        tem = True
                if tem:
                    temp.append(TextBlob(bounds[i][1]).detect_language()) if len(bounds[i][1]) >= 3 else temp.append('')
                else:
                    temp.append('en')
        image_with_bounds = draw_boxes(image, bounds)
        buffered = io.BytesIO()
        image_with_bounds.save(buffered, format="png")
        b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        text_trans = []
        app.logger.info(bounds)
        app.logger.info(temp)
        for i in range(len(temp)):
            if temp[i] in ['te', 'hi', 'ta', 'ka'] and bounds[i][2] > 0.001:
                translator = Translator(from_lang=temp[i] + '-IN', to_lang='en')
                translation = translator.translate(bounds[i][1])
                text_trans.append(translation.upper())
            else:
                if bounds[i][2] > 0.001:
                    text_trans.append(bounds[i][1])
        text = "\n".join([i[1] if i[2] > 0.001 else '' for i in bounds])
        text_trans = '\n'.join(text_trans)
        return render_template('result.html', image="data:image/png;base64," + b64, text=text, text_trans=text_trans)
    return render_template('index.html', form=form)


@app.route('/test')
def test():
    return render_template('result.html', text="hello  there", image='null')
