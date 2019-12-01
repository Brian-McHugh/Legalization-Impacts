import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Legalization_data.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
State_Metadata = Base.classes.useyr_891617
State_Arrest = Base.classes.arrest_prispop_data


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(State_Arrest).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<state>")
def useyr_891617(state):
    """Return the MetaData for a given sample."""
    sel = [
        State_Metadata.State,
        State_Metadata.age1217_89,
        State_Metadata.age1217_1617,
        State_Metadata.age1825_89,
        State_Metadata.age1825_1617,
        State_Metadata.age26_89,
        State_Metadata.age26_1617,
    ]

    results = db.session.query(*sel).filter(State_Metadata.state == state).all()

    # Create a dictionary entry for each row of metadata information
    useyr_891617 = {}
    for result in results:
        useyr_891617["State"] = result[0]
        useyr_891617["age1217_89"] = result[1]
        useyr_891617["age1217_1617"] = result[2]
        useyr_891617["age1825_89"] = result[3]
        useyr_891617["age1825_1617"] = result[4]
        useyr_891617["BBTYPE"] = result[5]
        useyr_891617["age26_89"] = result[6]
        useyr_891617["age26_1617"] = result[7]

    print(useyr_891617)
    return jsonify(useyr_891617)


@app.route("/arrest_prispop_data/<state>")
def arrest_prispop_data(state):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(State_Arrest).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    state_data = df.loc[df[state] > 1, ["dt_ids", "dt_information", state]]

    # Sort by sample
    state_data.sort_values(by=state, ascending=False, inplace=True)

    # Format the data to send as json
    data = {
        "dt_ids": state_data.dt_id.values.tolist(),
        "sample_values": state_data[state].values.tolist(),
        "dt_information": state_data.dt_information.tolist(),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()

