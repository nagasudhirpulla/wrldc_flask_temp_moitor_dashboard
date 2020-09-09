'''
This is the web server that acts as a service that creates outages raw data
'''
from src.config.appConfig import getConfig
from flask import Flask, request, jsonify, render_template
from src.services.tempHumApiFetcher import TempHumApiFetcher
import datetime as dt
from waitress import serve

app = Flask(__name__)

# get application config
appConfig = getConfig()

# Set the secret key to some random bytes
app.secret_key = appConfig['flaskSecret']
tokenUrl: str = appConfig['tokenUrl']
apiBaseUrl: str = appConfig['apiBaseUrl']
clientId: str = appConfig['clientId']
clientSecret: str = appConfig['clientSecret']

tempHumFetcher = TempHumApiFetcher(
    tokenUrl, apiBaseUrl, clientId, clientSecret)

@app.route('/api/<measId>/<startTime>/<endTime>')
def deviceDataApi(measId: str, startTime: str, endTime: str):
    startDt = dt.datetime.strptime(startTime, '%Y-%m-%d-%H-%M-%S')
    endDt = dt.datetime.strptime(endTime, '%Y-%m-%d-%H-%M-%S')
    resData = tempHumFetcher.fetchData(measId, startDt, endDt)
    return jsonify(resData)

@app.route('/')
def home():
    return render_template('home.html.j2')

if __name__ == '__main__':
    serverMode: str = appConfig['mode']
    if serverMode.lower() == 'd':
        app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    else:
        serve(app, host='0.0.0.0', port=int(appConfig['flaskPort']), threads=1)
