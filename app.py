import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import MetaData

app = Flask(__name__)
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)





@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"api/v1.0/start<br/>"
        f"/api/v1.0<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    results = session.query(Measurement.date, Measurement.prcp).all()
    result_dict = dict(results)
    return jsonify(result_dict)

@app.route('/api/v1.0/stations')
def stations():

    results = session.query(Stations.stations).all()
    results_list = list(results)
    return jsonify(results_list)

@app.route('/api/v1.0/tobs')
def tobs():
    todays_date = date.today()
    results = session.querry(Measurement.tobs).filter(func.date(Measurement.date) >= date(todays_date.year-2, todays_date.month, todays_date.day)).groupby(Measurement.date()).all()
    results_list = list(results)
    return jsonify(results_list)


# @app.route('/api/v1.0/start')
# def start():
#     results = session.query((Measurement.date, func.min(Measurement.tobs()), func.max(Measurement.tobs()), func.avg(Measurement.tobs()).filter(func.date(Measeurment.date() >= func.date(start))).group_by(Measurement.date).all()