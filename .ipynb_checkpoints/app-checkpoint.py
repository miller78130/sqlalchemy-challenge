import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify



#Bring in dictionaries here

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station





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
# Convert the query results to a dictionary using date as the key and prcp as the value.    
    session = Session(engine)
    
    precip_last = session.query(Measurement.prcp, Measurement.date).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()
    
    session.close()
    
    precip_dict = list(np.ravel(precip_last))
    
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
