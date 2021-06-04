import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify



#Bring in dictionaries here


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to My Vacation Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>
        f"/api/v1.0/<start>/<end>
    )


# 4. Define what to do when a user hits the different routes

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    return jsonify(precip_dict)




@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page ...")
    return jsonify(station_dict)




@app.route("/api/v1.0/tobs")
def stations():
    print("Server received request for 'tobs' page ...")
    return jsonify(tobs_dict)



@app.route("/api/v1.0/<start>")
def stations():
    print("Server received request for 'start' page ...")
    return jsonify(start_dict)



@app.route("/api/v1.0/<start>/<end>")
def stations():
    print("Server received request for 'start/end' page ...")
    return jsonify(start_end_dict)




if __name__ == "__main__":
    app.run(debug=True)
