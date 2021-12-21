# Import Dependencies
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create route that renders index.html template and finds mars app from mongo
@app.route("/")
def index():
    
    # find Mars data
    mars_info_scrape = mongo.db.mars_data.find_one()
    
    # return template and data
    return render_template("index.html", mars_info_scrape=mars_info_scrape)

@app.route("/scrape")
def scrape():
        mars_info_scrape = mongo.db.mars_data
        mars_data = scrape_mars.scrape_mars_news()
        mars_data = scrape_mars.scrape_mars_image()
        mars_data = scrape_mars.scrape_mars_facts()
        mars_data = scrape_mars.scrape_mars_hemispheres()
        mars_info_scrape.update({}, mars_data, upsert=True)
        
        return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
