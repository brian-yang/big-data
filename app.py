from flask import Flask, render_template, request, session, redirect, url_for
from utils import billionaires, global_development, state_fragility

app = Flask(__name__)
app.secret_key = 'dogsrcool'

countries_list = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 'Japan', 'Mexico', 'Philippines', 'Ethiopia', 'Vietnam','Egypt', 'Iran', 'Germany', 'Turkey', 'Thailand', 'France', 'United Kingdom', 'Italy', 'Burma', 'South Africa']
@app.route('/')
def root():
    #blist = billionaires.get_billionaires()[:10]
    gd_list = []
    for country in countries_list:
        data = global_development.get_reports_by_country(country)
        if len(data) <=0:
            continue
        else:
            data = data[0]
        gd_list.append([data['Country'], float(data['Data']['Urban Development']['Urban Population Percent'] )])
    return render_template("index.html", gd_list=gd_list)

@app.route('/test/')
def test():
    # for value in state_fragility.get_scores():
    #     print
    #     print value
        # print value['Metrics']['State Fragility Index']
        # print value['Metrics']['Country']
        # print value['Metrics']['Year']
    return render_template("index2.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
