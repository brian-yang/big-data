from flask import Flask, render_template, request, session, redirect, url_for
from utils import billionaires, global_development, state_fragility

app = Flask(__name__)
app.secret_key = 'dogsrcool'

countries_list = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 'Japan', 'Mexico', 'Philippines', 'Ethiopia', 'Vietnam','Egypt', 'Iran', 'Germany', 'Turkey', 'Thailand', 'France', 'United Kingdom', 'Italy', 'Burma', 'South Africa']
@app.route('/')
def root():
    b_data = billionaires.get_billionaires()
    b_list = []
    gd_list = []
    sf_list = []
    sf_data =  state_fragility.get_scores()
    for sf in sf_data:
        if sf['Country'] in countries_list and sf['Country'] not in sf_list:
            sf_list.append([sf['Country'], sf['Metrics']['State Fragility Index']])
    for billionaire in b_data:
        b_list.append([billionaire['name'], billionaire['location']['citizenship']])
    for country in countries_list:
        data = global_development.get_reports_by_country(country)
        if len(data) <=0:
            continue
        else:
            data = data[0]
        gd_list.append([data['Country'], float(data['Data']['Urban Development']['Urban Population Percent'] )])
    return render_template("index.html", gd_list=gd_list, sf_list=sf_list)

@app.route('/test/')
def test():
    return render_template("index2.html")

@app.route('/linegraphdata/<country>'):
def jsonLineGraph(country):
    for value in state_fragility.get_scores():
        sf_index = value['Metrics']['State Fragility Index']
        country = value['Country']
        year = value['Year']
        # print "%s\n%s\n%s" % (sf_index, country, year)
        print "%s,%s" % (year,sf_index)

    return render_template("jsonLineGraph.html", country = country)

if __name__ == '__main__':
    app.debug=True
    app.run()
