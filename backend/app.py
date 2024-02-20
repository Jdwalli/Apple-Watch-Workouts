import datetime
from flask import Flask, request, jsonify
from zipfile import ZipFile
from utils.file_utils import DataFile
from processors.apple_health_export import AppleHealthExport
from utils import file_utils as file_utils
from utils import response_utils as response_utils
from utils import time_utils as time_utils

FLASK_CONFIG = {
    "DEBUG": True,
}

DATA_FILE_HANDLER = DataFile()
app = Flask(__name__)
app.config.from_mapping(FLASK_CONFIG)


""" ================ DATA UPLOAD AND STATUS ROUTES ================ """
@app.route("/api/data-status", methods=["GET"])
def start_data_status():
    return jsonify({
        'dataPresent': DATA_FILE_HANDLER.containsData()
    }), 200

@app.route("/api/upload", methods=["POST"])
def upload():
    upload_time = datetime.datetime.now()
    uploadedFile = request.files
    uploadedZip = uploadedFile['file']
    with ZipFile(uploadedZip, "r") as zipFile:
        files = zipFile.infolist()
        for file in files:
            file_name = file.filename
            if not file_name.startswith('apple_health_export/'):
                return jsonify({'Error': 'This is not a Apple Health Export'}), 400
        AppleHealthExport(
            uploadedZip, 'apple_health_export/').parse_health_data()
    end_time = datetime.datetime.now()
    return jsonify({
        'Response': {'Message': 'File successfully uploaded and parsed', 'Timestamp': {
            "uploadTime": upload_time, "endTime": end_time, 'duration': {'timeTaken': time_utils.calculate_time_delta(upload_time, end_time), 'unit': 'seconds'}
        }}
    }), 200

""" ================ USER DATA ROUTES ================ """
@app.route("/api/user-record", methods=["GET"])
def send_extracted_user_data():
    return NotImplementedError


""" ================ RECORD ROUTES ================ """
@app.route("/api/records", methods=["GET"])
def send_record_type_data():
    return NotImplementedError

@app.route("/api/record-by-type", methods=["POST"])
def send_record_by_type_data():
    post_data = request.get_json()
    return NotImplementedError

@app.route("/api/record-by-dates", methods=["POST"])
def send_record_by_dates_data():
    post_data = request.get_json()
    return NotImplementedError

""" ================ ACTIVITY SUMMARY ROUTES ================ """
@app.route("/api/activity-summary", methods=["POST"])
def send_specific_activity_summary():
    post_data = request.get_json()
    return NotImplementedError

@app.route("/api/activity-summaries", methods=["GET"])
def send_all_activity_summaries():
    return NotImplementedError

""" ================ WORKOUT DATA ROUTES ================ """
@app.route("/api/all-workout-details", methods=["GET"])
def send_all_workout_details():
    return NotImplementedError

@app.route("/api/workout-types", methods=["GET"])
def send_all_workouts():
    return NotImplementedError

@app.route("/api/workouts-breakdown-statistics", methods=["GET"])
def send_workout_breakdown_statistics():
    return NotImplementedError

@app.route("/api/workouts-statistics", methods=["GET"])
def send_workout_statistics():
    return NotImplementedError

@app.route("/api/workout", methods=["POST"])
def send_specific_workout():
    return NotImplementedError

if __name__ == "__main__":
    DATA_FILE_HANDLER.create_data_directories()
    app.run(debug=True)

