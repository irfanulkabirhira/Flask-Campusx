from flask import Flask , render_template
# Create the Flask App

app = Flask(__name__ , )

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")




# To Start the Applicaiton
if __name__ == "__main__":
    app.run(debug=True)
