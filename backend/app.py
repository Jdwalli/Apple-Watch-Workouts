import datetime 
from flask import Flask, request, jsonify

app = Flask(__name__)

""" ================ USER DATA ROUTES ================ """
@app.route("/api/user-record", methods=["GET"])
def send_extracted_user_data():
    return NotImplementedError

""" ================ DATA UPLOAD ROUTE ================ """
@app.route("/api/upload", methods=["POST"])
def upload_extracted_file():
    return NotImplementedError


""" ================ WORKOUT DATA ROUTE ================ """
@app.route("/api/workout", methods=["POST"])
def send_requested_workout():
    return NotImplementedError

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



if __name__ == "__main__":
    app.run(debug=True)