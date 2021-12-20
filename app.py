# Import Dependencies
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create route that renders index.html template and finds mars app from mongo
@app.route("/")
def index():
    
    # find Mars data
    mars_data = mongo.db.mars_data.find_one()
    
    # return template and data
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
        mars_data = mongo.db.mars_data
        mars_news = scrape_mars.scrape_mars_news()
        mars_image = scrape_mars.scrape_mars_image()
        mars_facts = scrape_mars.scrape_mars_facts()
        mars_hemispheres = scrape_mars.scrape_mars_hemispheres()
        mars_data.update({}, mars_data, upsert=True)
        
        return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
