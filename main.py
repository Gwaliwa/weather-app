from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

files = "/Users/gmashaka/Documents/myprojects/weather-app/data_small/stations.txt"
stations = pd.read_csv(files, skiprows=17)
stations = stations[["STAID","STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html", data = stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "/Users/gmashaka/Documents/myprojects/weather-app/data_small/TG_STAID"+station.zfill(6)+".txt"

    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station, "date": date, "temperature": temperature
            }

if __name__ == "__main__":
    app.run(debug=True)