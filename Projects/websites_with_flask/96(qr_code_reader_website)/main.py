from __future__ import print_function
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import cloudmersive_barcode_api_client
from cloudmersive_barcode_api_client.rest import ApiException

import os


UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = tuple(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)

CLOUD_MERSIVE_API_KEY = YOUR_CLOUD_MERSIVE_API_KEY


def scan_qr(path) -> dict[str, str]:
    # Configures API key authorization: Apikey
    configuration = cloudmersive_barcode_api_client.Configuration()
    configuration.api_key['Apikey'] = CLOUD_MERSIVE_API_KEY

    # creates an instance of the API class
    api_instance = cloudmersive_barcode_api_client.BarcodeScanApi(cloudmersive_barcode_api_client.ApiClient(configuration))
    image_file = f"{path}"  # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.
    image_file = image_file.replace(" ", "_")
    try:
        # Scans and recognize an image of a barcode
        api_response = api_instance.barcode_scan_image(image_file)
        return api_response
    except ApiException as e:
        print("Exception when calling BarcodeScanApi->barcode_scan_image: %s\n" % e)


@app.route('/')
def home():
    return redirect(url_for('upload_file'))


def allowed_file(filename: str) -> bool:
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
            image_path = f"{UPLOAD_FOLDER}/{file.filename}"
            image_path = image_path.replace(" ", "_")
            return redirect(url_for('show_scanned', image_path=image_path))
    return render_template('upload.html')


@app.route("/show", methods=['GET', 'POST'])
def show_scanned():
    image_path = request.args.get('image_path')
    scanned_value = scan_qr(image_path)
    return render_template('show.html', image_path=image_path, scanned_value=scanned_value)


if __name__ == '__main__':
    app.run(debug=True)
