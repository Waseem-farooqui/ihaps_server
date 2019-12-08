# Running Instructions
# Go to the IHaps folder
# Run command from the terminal pip3 -r requirements.txt
# Run the command flask run --host 0.0.0.0
# Check you IP address in Linux ifconfig in Windows ipconfig

import json
from datetime import datetime

from flask import Flask, request, Response, jsonify

app = Flask(__name__)


# @Author Fawad Farooqui
# @Project IHaps

# The function is the REST endpoint that would be triggered
# when the device sends the post request having body of beat and patient in it.
@app.route('/beat', methods=['POST'])
def beat():
    data = request.json
    if data is not None:
        beat = int(data['beat'])
        patient = data['patient']
        dat = str(datetime.today())
        print(dat)
        resp = json.dumps({"beat": beat, "patient": patient, "time": dat})
        return Response(resp, status=200, mimetype="application/json")
    resp_msg = "{'error': 'Beat and patient is required in data.'}"
    return Response(resp_msg, status=400, mimetype="application/json")


# This function is used by the Android Application and the
# Web application that would be triggered when it would be asked for the data.
@app.route('/beat', methods=['GET'])
def new_beat():
    patient = request.args.get("patient")
    if patient is not None:
        dat = str(datetime.today())
        print(dat)
        resp = json.dumps({"beat": 67, "patient": patient, "time": dat})
        return Response(resp, status=200, mimetype="application/json")
    resp_msg = "{'error': 'Beat and patient is required in data.'}"
    return Response(resp_msg, status=400, mimetype="application/json")


if __name__ == '__main__':
    app.run()
