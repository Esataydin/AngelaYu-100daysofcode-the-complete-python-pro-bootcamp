from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from PIL import Image
from colorthief import ColorThief
import webcolors

import os


UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = tuple(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


@app.route('/')
def home():
    return redirect(url_for('upload_file'))


def allowed_file(filename) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # checks if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = f"../{UPLOAD_FOLDER}/{file.filename}"
            return redirect(url_for('show_hex_codes', image_path=image_path))
    return render_template('upload.html')


@app.route('/show', methods=['GET', 'POST'])
def show_hex_codes():
    image_path = request.args.get('image_path')
    new_filepath = image_path.replace('../', '')
    image_colors = []
    with open(new_filepath, 'r+b') as f:
        with Image.open(f) as image:
            # Gets Colors
            color_thief = ColorThief(new_filepath)
            color_palette = color_thief.get_palette(color_count=10, quality=10)
            for color in color_palette:
                image_colors.append(webcolors.rgb_to_hex(color).upper())
    # Displays picture's colors' HEX codes with picture
    return render_template('show.html', image_path=image_path, colors=image_colors)


if __name__ == '__main__':
    app.run(debug=True)
