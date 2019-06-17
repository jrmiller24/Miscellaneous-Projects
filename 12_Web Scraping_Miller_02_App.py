 # Import Dependencies 

from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

 # Create an instance of Flask
app = Flask(__name__)

 # Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

 # Route to render index.html template using data from Mongo
@app.route("/")
def home():

     # Find one record of data from the mongo database
     destination_data = mongo.db.collection.find_one()

     # Return template and data
     return render_template("index.html", space=destination_data)


 # Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

     # Run the scrape function
     data = scrape_mars.scrape_all()
     # return jsonify(data)
     # Update the Mongo database using update and upsert=True
     mongo.db.collection.update({}, data, upsert=True)

     # Redirect back to home page
     return redirect("/")



if __name__ == "__main__":
     app.run(debug=True)

#  import dependencies

# from flask import Flask, render_template
# from flask_pymongo import PyMongo
# import scrape_mars

# # create flask
# app = Flask(__name__)

# #Use pymongo to create a mongodb connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)


# @app.route("/")
# def home():
#    mars_data = mongo.db.mars_data.find_one()
#    return(render_template("index.html", mars=mars_data))

# # route to trigger scrape
# @app.route("/scrape")
# def scrape():
#    #run scrape
#    mars_scrape_data = scrape_mars.scrape_all()
#    #update mongo db with scraped data
#    mongo.db.mars_data.update({}, mars_scrape_data, upsert=True)
#    #print successful scrape on the pagee
#    return ("successful scrape")


# if __name__=="__main__":
#    app.run()