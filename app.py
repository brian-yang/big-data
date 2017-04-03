from flask import Flask, render_template, request, session, redirect, url_for, Response
from utils import billionaires, global_development, state_fragility
import json, urllib2, urllib

app = Flask(__name__)
app.secret_key = 'dogsrcool'

# =============================
# MAIN
# =============================
key = 'AIzaSyBWmidBiLAZAKmAaEitHqolV6URd_yOsAY'
countries_list = ['India', 'China', 'United States', 'Russia', 'Canada', 'Brazil', 'Argentina', 'Colombia', 'Australia', 'South Africa', 'Madagascar', 'Germany']
countries_list2 = ['IND', 'CHN', 'USA', 'RUS', 'CAN', 'BRA', 'ARG', 'COL', 'AUS', 'ZAF', 'MAD', 'DEU']
@app.route('/', methods = ['GET', 'POST'])
def root():
    # Map

    b_data = billionaires.get_billionaires()
   # print b_data[:5]
    b_dict = {}
    gd_list = []
    sf_list = []
    sf_data =  state_fragility.get_scores()
    used_list = []
    for sf in sf_data:
        if sf['Country'] in countries_list and sf['Country'] not in used_list:
            sf_list.append([countries_list2[countries_list.index(sf['Country'])], sf['Metrics']['State Fragility Index']])
            used_list.append(sf['Country'])
    for billionaire in b_data:
        nation = billionaire['location']['country code']
        if nation in countries_list2:
            location = geo_loc(nation)
            if nation in b_dict:
                b_dict[nation][0]+=1
            else:
                b_dict[nation] = [0, location]
    for a in b_dict:
        print a
        break
    ##print "CHINA", b_dict['CHN']
        #b_list.append([billionaire['name'], billionaire['location']['country code']])
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

    return render_template("dots.html", gd_list=gd_list, sf_list=sf_list, b_dict=b_dict, countries=countries_list, line_graph_country = line_graph_country)

# =============================
# LINE GRAPH ROUTES
# =============================

# line graph can only read data from this route if it includes a
# .json extension at the end of the country name
@app.route('/line/development/<country>.json/')
def development(country):
    data = []

    for value in global_development.get_reports():
        if country == value['Country']:
            telephone_lines = round(value['Data']['Infrastructure']['Telephone Lines per 100 People'], 3)
            cell_subscriptions = round(value['Data']['Infrastructure']['Mobile Cellular Subscriptions per 100 People'], 3)
            life_expectancy = round(value['Data']['Health']['Life Expectancy at Birth, Total'], 3)

            measure_growth = round((cell_subscriptions + telephone_lines) * life_expectancy)
            year = value['Year']
            data.append({'index': measure_growth , 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')

@app.route('/line/fragility/<country>.json/')
def fragility(country):
    data = []

    for value in state_fragility.get_scores():
        if country == value['Country']:
            sf_index = value['Metrics']['State Fragility Index']
            year = value['Year']
            data.append({'index': sf_index, 'date': year})

    return Response(response = json.dumps(data), status = 200, mimetype='application/json')

# =============================
# MAP
# =============================

def geo_loc(location):
#finds the longitude and latitude of a given location parameter using Google's Geocode API
#return format is a dictionary with longitude and latitude as keys
        loc = urllib.quote_plus(location)
        googleurl = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (loc,key)
        request = urllib2.urlopen(googleurl)
        results = request.read()
        gd = json.loads(results) #dictionary
        if gd['status'] != "OK":
                return location+" is a bogus location! What are you thinking?"
        else:
                result_dic = gd['results'][0] #dictionary which is the first element in the results list
                geometry = result_dic['geometry'] #geometry is another dictionary
                loc = geometry['location'] #yet another dictionary
                return loc

if __name__ == '__main__':
    app.debug=True
    app.run()
