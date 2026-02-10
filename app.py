from flask import Flask
from flask import render_template

# Create an instance of Flask 
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index():
    # Pass variables from Python to HTML!
    name_data = None
    return render_template("index.html", name=name_data)

# TO RUN YOUR APP enter "flask run" into the TERMINAL
# (if you closed your terminal, open it again with CTRL + `)
# TO STOP click CTRL + C in the TERMINAL
