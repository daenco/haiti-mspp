from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
	# return redirect(url_for("login"))
	return render_template("index.html",
			               title="Index")


@app.route("/login")
def login():
	return render_template("login.html",
						   title="Login")


@app.route("/institutions")
def institution():
	return render_template("institution/index.html",
		                   title="Institutions")


@app.errorhandler(404)
def not_found(error):
	return render_template("404.html", 
						   title="404 Page Error")


if __name__ == "__main__":
	app.run(debug=True)