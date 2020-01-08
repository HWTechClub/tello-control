from flask import Flask
import tellopy


app = Flask(__name__)

# Configurations for the tello drone
try:
   drone = tellopy.Tello()
   drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
   drone.connect()
   drone.wait_for_connection(60.0)
   drone.set_alt_limit(2)
except Exception as ex:
    print("drone not connected or enjoy debugging your error")

# Routing for controlling the drone 
@app.route("/takeoff")# Number can be # Number can be modified modified 
def takeoff(): 
    try:
        drone.takeoff()
    except Exception as ex:
        return "fail"
    return "success"

@app.route("/land")
def land():
    try:
        drone.land()
    except Exception as ex:
        return "fail"
    return "success"

@app.route("/up")
def up():
    try:
        drone.up(20)  # Number can be modified 
    except Exception as ex:
        return "fail"
    return "success"

@app.route("/down")
def down():
    try:
        drone.down(20) # Number can be modified 
    except Exception as ex:
        return "fail"
    return "success"

