from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app=Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = 'mongodb+srv://vic_user_26:v!cky!99!&!989@myfirstcluster-ziitx.mongodb.net/recipes_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("get_recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
    