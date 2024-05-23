from flask import Flask, render_template, request
import requests
import os 
from deeplearning import OCR
# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

@app.route('/vehicleEnquiry/<reg_no>',methods=['POST','GET'])
def fetch_vehicle_info(reg_no):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"

    payload = {
        "reg_no": reg_no,
        "consent": "Y",
        "consent_text": "I hear by declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9ab4215ba3msh95258bd41684986p1df508jsn7cdc3f323831",
        "X-RapidAPI-Host": "rto-vehicle-information-verification-india.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json();
    # print(data);
    return render_template('vehicle_details.html',upload=False,data=data)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)

        return render_template('index.html',upload=True,upload_image=filename,text=text)

    return render_template('index.html',upload=False)


if __name__ =="__main__":
    app.run(debug=True)