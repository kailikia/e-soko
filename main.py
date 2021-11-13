from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import requests,json


app = Flask(__name__)
alvapi_key = "BA0DSY2O5I5S3ABT"
scheduler = BackgroundScheduler(daemon=True)

@app.route("/")
def index():
    # Make a GET Request to Alphavantage
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=' + alvapi_key)
    #Store the data received
    data = r.text
    #Find out type of data
    print(type(data))
    #Convert from string
    data_json = json.loads(data)
    #Find out type of data
    print(type(data_json))
    return render_template("index.html", stock_data = data_json['Weekly Time Series'])

def request_scheduler():
    print(datetime.datetime.now())

#Create the scheduler job
scheduler.add_job(request_scheduler, 'interval', minutes=1)
#start the scheduler
scheduler.start()

    

if __name__ == "__main__":
    app.run()