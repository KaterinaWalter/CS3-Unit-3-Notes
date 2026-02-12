from flask import Flask
from flask import render_template

# Create an instance of Flask 
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index():
    # Pass variables from Python to HTML!
    name_data = 'Katerina'
    year_data = 2026
    # Can also use lists & dictionaries
    favorites_list = ['Pokemon', 'Baldurs Gate', 'The Sims', 'Zelda' ]
    ratings_dict = { 'Pokemon Legends Arceus' : 'I love every classic Pokemon game, but the catching mechanic in this one was especially fun.', 
                     'BG3' : 'Baldurs Gate 3 was Game of the Year for a reason! Got me into the world of D&D.', 
                     'The Sims 4': 'Unplayable without mods, but timeless fun.',
                     'Tears of the Kingdom': "My first Zelda game, loved it, and now wishing I've been a fan since the beginning." }
    # name is how we refer to it in the HTML template,
    # name_data is the variable declared here in Python
    return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict)

# TO RUN YOUR APP enter "flask run" into the TERMINAL
# (if you closed your terminal, open it again with CTRL + `)
# TO STOP click CTRL + C in the TERMINAL
