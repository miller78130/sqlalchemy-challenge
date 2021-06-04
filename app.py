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
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/precip/01-01<br/>"
        f"/api/v1.0/precip/2016-03-20/2016-03-30<br/>"
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
 #   Return a JSON list of stations from the dataset.
    session = Session(engine)

    stations = session.query(Station.station).all()

    session.close()

    station_dict = stations


    return jsonify(station_dict)




@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page ...")
    
    session = Session(engine)

    temp_last = session.query(Measurement.tobs).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()

    session.close()

    tobs_dict = temp_last
      
    
    return jsonify(tobs_dict)



@app.route("/api/v1.0/precip/<date>")
def precip_start(date):
    print("Server received request for 'start' page ...")
    
    session = Session(engine)  
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    
    
    precip = session.query(*sel).filter(func.strftime("%m-%d", Measurement.date) >= date).all()   
    
    session.close()

    return jsonify(precip)

#return jsonify({"error": f"Date out of Range or verify date format of mm-dd."}), 404

@app.route("/api/v1.0/precip/<start>/<end>")
def precip(start, end):
    print("Server received request for 'start/end' page ...")
    
    session = Session(engine)  
    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    
    
    precip1 = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    return jsonify(precip1)

#return jsonify({"error": f"Date out of Range or verify date format of yyyy-mm-dd."}), 404

if __name__ == "__main__":
    app.run(debug=True)
