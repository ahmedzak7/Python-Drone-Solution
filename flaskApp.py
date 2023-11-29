# app.py
from flask import Flask, request, jsonify
# import file and class Drone
from drone import Drone

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Drone, please move it on /move_drone endpoint"
@app.route('/move_drone', methods=['POST'])
def move_drone():
    data = request.json
    cube_dimensions = data['cube_dimensions']
    drone_data = data['drones']

    result = []

    for drone_position, drone_instructions in drone_data:
        drone = Drone(*drone_position)
        drone.move(drone_instructions)
        result.append(str(drone))

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
