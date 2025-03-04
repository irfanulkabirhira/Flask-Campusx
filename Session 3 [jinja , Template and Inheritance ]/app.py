from flask import Flask
# Create the Flask App

app = Flask(__name__)

# Home page
@app.route("/")
@app.route("/home")
def home():
    return "<h1> Welcome to the Home page ! </h1>"

# About Page
@app.route("/about")
def about():
    return "<h1> Welcome to the About page </h1>"




# To Start the Applicaiton
if __name__ == "__main__":
    app.run(debug=True)
