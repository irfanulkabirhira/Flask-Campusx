from flask import Flask , render_template, url_for
# Create the Flask App

app = Flask(__name__ , )

# Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

# About Page
@app.route("/about")
def about():
    return render_template("about.html", title = "About")




# To Start the Applicaiton
if __name__ == "__main__":
    app.run(debug=True)
