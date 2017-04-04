from flask import Flask, render_template, request, session, redirect, url_for, Response
from utils import billionaires, global_development, state_fragility, parser
import json, urllib2, urllib

app = Flask(__name__)
app.secret_key = 'dogsrcool'

# =============================
# MAIN
# =============================
countries_list =  ["Aruba", "Afghanistan", "Angola", "Anguilla", "Aland Islands", "Albania", "Andorra", "United Arab Emirates", "Argentina", "Armenia", "American Samoa", "Antarctica", "French Southern Territories", "Antigua and Barbuda", "Australia", "Austria", "Azerbaijan", "Burundi", "Belgium", "Benin", "Bonaire, Sint Eustatius and Saba", "Burkina Faso", "Bangladesh", "Bulgaria", "Bahrain", "Bahamas", "Bosnia and Herzegovina", "Saint Barthelemy", "Belarus", "Belize", "Bermuda", "Bolivia, Plurinational State of", "Brazil", "Barbados", "Brunei Darussalam", "Bhutan", "Bouvet Island", "Botswana", "Central African Republic", "Canada", "Cocos (Keeling) Islands", "Switzerland", "Chile", "China", "Cote d'Ivoire", "Cameroon", "Congo, the Democratic Republic of the", "Congo", "Cook Islands", "Colombia", "Comoros", "Cabo Verde", "Costa Rica", "Cuba", "Curacao", "Christmas Island", "Cayman Islands", "Cyprus", "Czechia", "Germany", "Djibouti", "Dominica", "Denmark", "Dominican Republic", "Algeria", "Ecuador", "Egypt", "Eritrea", "Western Sahara", "Spain", "Estonia", "Ethiopia", "Finland", "Fiji", "Falkland Islands (Malvinas)", "France", "Faroe Islands", "Micronesia, Federated States of", "Gabon", "United Kingdom", "Georgia", "Guernsey", "Ghana", "Gibraltar", "Guinea", "Guadeloupe", "Gambia", "Guinea-Bissau", "Equatorial Guinea", "Greece", "Grenada", "Greenland", "Guatemala", "French Guiana", "Guam", "Guyana", "Hong Kong", "Heard Island and McDonald Islands", "Honduras", "Croatia", "Haiti", "Hungary", "Indonesia", "Isle of Man", "India", "British Indian Ocean Territory", "Ireland", "Iran, Islamic Republic of", "Iraq", "Iceland", "Israel", "Italy", "Jamaica", "Jersey", "Jordan", "Japan", "Kazakhstan", "Kenya", "Kyrgyzstan", "Cambodia", "Kiribati", "Saint Kitts and Nevis", "Korea, Republic of", "Kuwait", "Lao People's Democratic Republic", "Lebanon", "Liberia", "Libya", "Saint Lucia", "Liechtenstein", "Sri Lanka", "Lesotho", "Lithuania", "Luxembourg", "Latvia", "Macao", "Saint Martin (French part)", "Morocco", "Monaco", "Moldova, Republic of", "Madagascar", "Maldives", "Mexico", "Marshall Islands", "Macedonia, the former Yugoslav Republic of", "Mali", "Malta", "Myanmar", "Montenegro", "Mongolia", "Northern Mariana Islands", "Mozambique", "Mauritania", "Montserrat", "Martinique", "Mauritius", "Malawi", "Malaysia", "Mayotte", "Namibia", "New Caledonia", "Niger", "Norfolk Island", "Nigeria", "Nicaragua", "Niue", "Netherlands", "Norway", "Nepal", "Nauru", "New Zealand", "Oman", "Pakistan", "Panama", "Pitcairn", "Peru", "Philippines", "Palau", "Papua New Guinea", "Poland", "Puerto Rico", "Korea, Democratic People's Republic of", "Portugal", "Paraguay", "Palestine, State of", "French Polynesia", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saudi Arabia", "Sudan", "Senegal", "Singapore", "South Georgia and the South Sandwich Islands", "Saint Helena, Ascension and Tristan da Cunha", "Svalbard and Jan Mayen", "Solomon Islands", "Sierra Leone", "El Salvador", "San Marino", "Somalia", "Saint Pierre and Miquelon", "Serbia", "South Sudan", "Sao Tome and Principe", "Suriname", "Slovakia", "Slovenia", "Sweden", "Swaziland", "Sint Maarten", "Seychelles", "Syrian Arab Republic", "Turks and Caicos Islands", "Chad", "Togo", "Thailand", "Tajikistan", "Tokelau", "Turkmenistan", "Timor-Leste", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Tuvalu", "Taiwan, Province of China", "Tanzania, United Republic of", "Uganda", "Ukraine", "United States Minor Outlying Islands", "Uruguay", "United States of America", "Uzbekistan", "Holy See", "Saint Vincent and the Grenadines", "Venezuela, Bolivarian Republic of", "Virgin Islands, British", "Virgin Islands, U.S.", "Viet Nam", "Vanuatu", "Wallis and Futuna", "Samoa", "Yemen", "South Africa", "Zambia", "Zimbabwe"]

countries_list2 =  ["ABW", "AFG", "AGO", "AIA", "ALA", "ALB", "AND", "ARE", "ARG", "ARM", "ASM", "ATA", "ATF", "ATG", "AUS", "AUT", "AZE", "BDI", "BEL", "BEN", "BES", "BFA", "BGD", "BGR", "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ", "BMU", "BOL", "BRA", "BRB", "BRN", "BTN", "BVT", "BWA", "CAF", "CAN", "CCK", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK", "COL", "COM", "CPV", "CRI", "CUB", "CUW", "CXR", "CYM", "CYP", "CZE", "DEU", "DJI", "DMA", "DNK", "DOM", "DZA", "ECU", "EGY", "ERI", "ESH", "ESP", "EST", "ETH", "FIN", "FJI", "FLK", "FRA", "FRO", "FSM", "GAB", "GBR", "GEO", "GGY", "GHA", "GIB", "GIN", "GLP", "GMB", "GNB", "GNQ", "GRC", "GRD", "GRL", "GTM", "GUF", "GUM", "GUY", "HKG", "HMD", "HND", "HRV", "HTI", "HUN", "IDN", "IMN", "IND", "IOT", "IRL", "IRN", "IRQ", "ISL", "ISR", "ITA", "JAM", "JEY", "JOR", "JPN", "KAZ", "KEN", "KGZ", "KHM", "KIR", "KNA", "KOR", "KWT", "LAO", "LBN", "LBR", "LBY", "LCA", "LIE", "LKA", "LSO", "LTU", "LUX", "LVA", "MAC", "MAF", "MAR", "MCO", "MDA", "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MLT", "MMR", "MNE", "MNG", "MNP", "MOZ", "MRT", "MSR", "MTQ", "MUS", "MWI", "MYS", "MYT", "NAM", "NCL", "NER", "NFK", "NGA", "NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL", "OMN", "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL", "PRI", "PRK", "PRT", "PRY", "PSE", "PYF", "QAT", "REU", "ROU", "RUS", "RWA", "SAU", "SDN", "SEN", "SGP", "SGS", "SHN", "SJM", "SLB", "SLE", "SLV", "SMR", "SOM", "SPM", "SRB", "SSD", "STP", "SUR", "SVK", "SVN", "SWE", "SWZ", "SXM", "SYC", "SYR", "TCA", "TCD", "TGO", "THA", "TJK", "TKL", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV", "TWN", "TZA", "UGA", "UKR", "UMI", "URY", "USA", "UZB", "VAT", "VCT", "VEN", "VGB", "VIR", "VNM", "VUT", "WLF", "WSM", "YEM", "ZAF", "ZMB", "ZWE"]

@app.route('/', methods = ['GET', 'POST'])
def root():
    b_data = billionaires.get_billionaires()[:300]
    sf_data =  state_fragility.get_scores()

    b_dict = {}
    gd_list = []
    sf_list = []
    used_list = []

    # for sf in sf_data:
    #     if sf['Country'] in countries_list and sf['Country'] not in used_list:
    #         sf_list.append([countries_list2[countries_list.index(sf['Country'])], sf['Metrics']['State Fragility Index']])
    #         used_list.append(sf['Country'])

    # # BROKEN
    # for billionaire in b_data:
    #     nation = billionaire['location']['country code']
    #     if nation in countries_list2:
    #         location = geo_loc(billionaire['location']['citizenship'])
    #         #print location
    #         if nation in b_dict:
    #             b_dict[nation][0]+=1
    #         else:
    #             b_dict[nation] = [1, location['lat'], location['lng']]
    #for a in b_dict:
    #    print a
    #    break

    # BROKEN - don't know what this does
    #print "CHINA", b_dict['CHN']
    ##b_list.append([billionaire['name'], billionaire['location']['country code']])

    # for country in countries_list:
    #     data = global_development.get_reports_by_country(country)
    #     if len(data) <=0:
    #         continue
    #     else:
    #         data = data[0]
    #     gd_list.append([countries_list2[countries_list.index(data['Country'])], float(data['Data']['Urban Development']['Urban Population Percent'] )])

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
key = 'AIzaSyAA-qVR2isVAY5f8RDUGgsTw8qLtMeEekk'

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
    app.run(threaded=True)
