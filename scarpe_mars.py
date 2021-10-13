from logging import debug
from flask import Flask, render_template

import pymongo

app = Flask(__name__)

conn = 'mongod://localhost:27017'

client = pymongo.MongoClinet(conn)

db = client.mars_db

db.mars.drop()

mars_facts = [
    {"Equatorial Diameter": "6,792 km"},
    {"Polar Diameter:	": "6,752 km"},
    {"Mass:	": "6.39 × 10^23 kg (0.11 Earths)"},
    {"Moons:": "2 ( Phobos & Deimos )"},
    {"Orbit Distance:": "227,943,824 km (1.38 AU)"},
    {"Orbit Period:": "687 days (1.9 years)"},
    {"Surface Temperature:": "-87 to -5 °C"},
    {"First Record:": "2nd millennium BC"},
    {"Recorded By:": "Egyptian astronomers"}
]

@app.route("/")
def home():
    return render_template("index.html", mars=mars_facts)

if __name__ == "__main__":
    app.run(debug=True)