from flask import Flask, render_template, request, session, redirect, url_for, Response
from utils import billionaires, global_development, state_fragility
import json

app = Flask(__name__)
app.secret_key = 'dogsrcool'

# =============================
# MAIN
# =============================

countries_list = ['India', 'China', 'United States', 'Russia', 'Canada', 'Brazil', 'Argentina', 'Colombia', 'Australia', 'South Africa', 'Madagascar', 'Germany']
countries_list2 = ['IND', 'CHN', 'USA', 'RUS', 'CAN', 'BRA', 'ARG', 'COL', 'AUS', 'ZAF', 'MAD', 'DEU']
@app.route('/', methods = ['GET', 'POST'])
def root():
    # Map

    b_data = billionaires.get_billionaires()
    b_list = []
    gd_list = []
    sf_list = []
    sf_data =  state_fragility.get_scores()
    used_list = []
    for sf in sf_data:
        if sf['Country'] in countries_list and sf['Country'] not in used_list:
            sf_list.append([countries_list2[countries_list.index(sf['Country'])], sf['Metrics']['State Fragility Index']])
            used_list.append(sf['Country'])
    for billionaire in b_data:
        b_list.append([billionaire['name'], billionaire['location']['country code']])
    for country in countries_list:
        data = global_development.get_reports_by_country(country)
        if len(data) <=0:
            continue
        else:
            data = data[0]
        gd_list.append([countries_list2[countries_list.index(data['Country'])], float(data['Data']['Urban Development']['Urban Population Percent'] )])

    if "country" in request.form:
        line_graph_country = request.form["country"]
    else:
        line_graph_country = "default"

    return render_template("dots.html", gd_list=gd_list, sf_list=sf_list, countries=countries_list, line_graph_country = line_graph_country)

# =============================
# LINE GRAPH ROUTES
# =============================

# line graph can only read data from this route if it includes a
# .json extension at the end of the country name
@app.route('/linegraphdevelopment/<country>.json/')
def jsonLineGraph(country):
    data = []

    for value in global_development.get_reports():
        if country == value['Country']:
            percent_growth = (round(value['Data']['Urban Development']['Urban Population Percent Growth'] * 10)) / 10
            year = value['Year']
            data.append({'index': percent_growth , 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')

@app.route('/linegraphfragility/<country>.json/')
def jsonLineGraph2(country):
    data = []

    for value in state_fragility.get_scores():
        if country == value['Country']:
            sf_index = value['Metrics']['State Fragility Index']
            year = value['Year']
            data.append({'index': sf_index, 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')

if __name__ == '__main__':
    app.debug=True
    app.run()
