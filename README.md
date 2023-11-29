# Python-Drone-Solution
Drone Movement API
==================

This project implements a simple Flask API that allows users to control the movement of drones in a 3D space. The drones follow instructions to move forward, turn left or right, move up, and move down within a given cube's dimensions.

Table of Contents
-----------------

-   [Drone Class](https://chat.openai.com/c/ca098e1e-79a8-4de7-95af-b263b82ff4af#drone-class)
-   [Flask API](https://chat.openai.com/c/ca098e1e-79a8-4de7-95af-b263b82ff4af#flask-api)
-   [Getting Started](https://chat.openai.com/c/ca098e1e-79a8-4de7-95af-b263b82ff4af#getting-started)
-   [API Endpoints](https://chat.openai.com/c/ca098e1e-79a8-4de7-95af-b263b82ff4af#api-endpoints)
-   [Example Usage](https://chat.openai.com/c/ca098e1e-79a8-4de7-95af-b263b82ff4af#example-usage)

Drone Class
-----------

### `drone.py`

The `Drone` class represents a drone in a 3D space. It has the following attributes:

-   `x`: x-coordinate of the drone
-   `y`: y-coordinate of the drone
-   `z`: z-coordinate of the drone
-   `direction`: current facing direction of the drone (N, E, S, W)

The class provides methods for moving the drone based on a sequence of instructions:

-   `move(instructions)`: Move the drone according to a list of instructions.
-   `turn_left()`: Turn the drone 90 degrees to the left.
-   `turn_right()`: Turn the drone 90 degrees to the right.
-   `move_forward()`: Move the drone one unit forward in its current direction.
-   `move_up()`: Move the drone one unit up.
-   `move_down()`: Move the drone one unit down.
-   `__str__()`: Return a string representation of the drone's current state.

Flask API
---------

### `app.py`

The `app.py` file contains a Flask application that exposes two endpoints:

-   `/`: Home endpoint displaying a welcome message.
-   `/move_drone`: POST endpoint for moving drones. It takes JSON data containing cube dimensions and drone positions with instructions, processes the instructions, and returns the final positions of the drones.

Getting Started
---------------

1.  Clone the repository:

    bashCopy code

    `git clone <repository-url>
    cd <repository-folder>`

2.  Install dependencies:

    bashCopy code

    `pip install -r requirements.txt`

3.  Run the Flask application:

    bashCopy code

    `python3 app.py`

API Endpoints
-------------

### `/`

-   Method: GET
-   Description: Welcome message.

### `/move_drone`

-   Method: POST
-   Description: Move drones based on provided instructions.
-   Request Body:

    jsonCopy code

    `{
      "cube_dimensions": [width, height, depth],
      "drones": [
        [[x1, y1, z1, direction1], "instructions1"],
        [[x2, y2, z2, direction2], "instructions2"],
        ...
      ]
    }`

-   Response Body:

    jsonCopy code

    `[
      "final_position_drone1",
      "final_position_drone2",
      ...
    ]`

Example Usage
-------------
![postman](./Screenshot%2023-11-29%at%3.26.08%PM.png)

