import pandas as pd
import plotly.graph_objects as go

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///..Legalization_data.sqlite"

db = SQLAlchemy(app)

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/arrestprispop")
def arrestprispop ():
    
    # Query for the top 10 emoji data
    results = db.session.query(arrestprispop.Legalization_status17, arrestprispop.drugs100K_u18, arrestprispop.total100K_u18, arrestprispop.totnodrg100K_u18, arrestprispop.drugs100K_all, arrestprispop.total100K_all, arrestprispop.totnodrg100K_all).\
        order_by(arrestprispop.totnodrg100K_all.desc()).\
        limit(10).all

    df = pd.DataFrame(results, columns=['Legalization_status17', 'drugs100K_u18', 'total100K_u18', 'totnodrg100K_u18', 'drugs100K_all', 'total100K_all', 'totnodrg100K_all'])
       
    Legalization_status17 = df["Legalization_status17"].values.tolist()
    drug_arrests_u18 = df["drugs100K_u18"].valuse.tolist()
    all_arrests_u18 = df["total100K_u18"].valuse.tolist()
    allnodrug_arrests_u18 = df["totnodrg100K_u18"].valuse.tolist()
    drug_arrests_all = df["drugs100K_all"].valuse.tolist()
    all_arrests_all = df["total100K_all"].valuse.tolist()
    allnodrug_arrests_all = df["totnodrg100K_all"].valuse.tolist()

    # Generate the plot trace
    fig = go.Figure(data=[
        go.Bar(name='Under 18 Drug Arrests per 100K', x= Legalization_status17, y=drug_arrests_u18),
        go.Bar(name='Under 18 All Arrests per 100K', x=Legalization_status17, y=all_arrests_u18),
        go.Bar(name='Under 18 All Arrests (no drugs) per 100K', x=Legalization_status17, y=allnodrug_arrests_u18),
        go.Bar(name='All ages Drug Arrests per 100K', x= Legalization_status17, y=drug_arrests_all),
        go.Bar(name='All ages All Arrests per 100K', x=Legalization_status17, y=all_arrests_all),
        go.Bar(name='All ages All Arrests (no drugs) per 100K', x=Legalization_status17, y=allnodrug_arrests_all),
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()
    return jsonify(fig)


@app.route("/useyr_891617_grpleg")
def useyr_891617_grpleg ():
    
    # Query for the emoji data using pandas
    results = db.session.query(useyr_891617_grpleg.Legalization_status17, useyr_891617_grpleg.age1217_89, useyr_891617_grpleg.age1217_1617, useyr_891617_grpleg.age1825_89, useyr_891617_grpleg.age1825_1617, useyr_891617_grpleg.age26_89, useyr_891617_grpleg.age26_1617).\
        order_by(useyr_891617_grpleg.age1217_89.desc()).\
        limit(10).all
    
    df = pd.DataFrame(results, columns=['Legalization_status17', 'age1217_89', 'age1217_1617', 'age1825_89', 'age1825_1617', 'age26_89', 'age26_1617'])
    
    Legalization_status17 = df["Legalization_status17"].values.tolist()
    use1217_89 = df["age1217_89"].valuse.tolist()
    use1217_1617 = df["age1217_1617"].valuse.tolist()
    use1825_89 = df["age1825_89"].valuse.tolist()
    use1825_1617 = df["age1825_1617"].valuse.tolist()
    use26_89 = df["age26_89"].valuse.tolist()
    use26_1617 = df["age26_1617"].valuse.tolist()
    
    # Format the data for Plotly
    fig = go.Figure(data=[
        go.Bar(name='Use in last year 12-17-2008-2009', x= Legalization_status17, y=use1217_89),
        go.Bar(name='Use in last year 12-17-2016-2017', x=Legalization_status17, y=use1217_1617),
        go.Bar(name='Use in last year 18-25-2008-2009', x=Legalization_status17, y=use1825_89),
        go.Bar(name='Use in last year 18-25-2016-2017', x= Legalization_status17, y=use1825_1617),
        go.Bar(name='Use in last year 26+-2008-2009', x=Legalization_status17, y=use26_89),
        go.Bar(name='Use in last year 26+-2016-2017', x=Legalization_status17, y=use26_1617),
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()
    return jsonify(fig)

@app.route("/pop_private")
def pop_private():
   
    # Query for the top 10 emoji data
    results = db.session.query(arrestprispop.Legalization_status17, arrestprispop.pop_private2017).\
        order_by(arrestprispop.pop_private2017.desc()).\
        limit(10).all()
    df = pd.DataFrame(results, columns=['Legalization_status17', 'pop_private2017'])
    
    Legalization_status17 = df["Legalization_status17"].values.tolist()
    pop_private2017 = df["pop_private2017"].valuse.tolist()
        
    # Format the data for Plotly
    fig = go.Figure(data=[
        go.Bar(name='Population in Private Prisons', x= Legalization_status17, y=pop_private2017),
     ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()
    return jsonify(fig)

if __name__ == '__main__':
    app.run(debug=True)
