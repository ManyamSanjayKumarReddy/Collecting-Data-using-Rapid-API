import requests
import json

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

querystring = {"date":"2020-04-07"}

headers = {
	"X-RapidAPI-Key": "75296dc20dmsh63fba10cd8681dcp1f0aeajsn2df4b6ad72c9",
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.text

json_data = json.loads(data)

with open('total_report.json', 'w') as json_file:
    json.dump(json_data,json_file)