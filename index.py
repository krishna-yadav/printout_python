from flask import Flask , render_template

app = Flask(__name__)

@app.route("/page1")
def page1():
	print("hrllo")
	return render_template("page1.html")


@app.route("/page2")
def page2():
	print("hrllo")
	return render_template("page2.html")

@app.route("/page3")
def page3():
	print("hrllo")
	return render_template("page3.html")

app.run(debug=True)