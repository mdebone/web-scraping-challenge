# Import Dependencies
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Create route that renders index.html template and finds mars app from mongo
@app.route("/")
def home():
    
    # find Mars data
    mars_info_scrape = mongo.db.collection.find_one()
    
    # return template and data
    return render_template("index.html", mars=mars_info_scrape)

@app.route("/scrape")
def scrape():
        mars_info_scrape = mongo.db.mars_info_scrape
        mars_data = scrape_mars.scrape()
        mars_info_scrape.update({}, mars_data, upsert=True)
        
        return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
