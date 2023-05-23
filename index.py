from flask import Flask , render_template, request,redirect , url_for
import os 
from werkzeug.utils import secure_filename
from os.path import join

app = Flask(__name__)



@app.route("/page1" , methods = ['GET','POST'])
def page1():
	print("hello")

	if request.method == "POST":
		username = request.form['C_name']
		phone = request.form['C_mobile']
		email = request.form['C_email']
		print(username, phone , email)
		Upload_File = request.files['p1_fname']
		Upload_Link = request.form.get("p1_link", False)
		print(Upload_File.filename)
		enquiry =  request.form.get("enquiry", False)

		if enquiry == "enquiry" :
			return render_template("goodbye.html", enquiry = enquiry)

		user_folder = os.path.join("C:\\Users\\admin\\OneDrive\\Documents\\Kiran\\new")
		Upload_File.save(join(user_folder, secure_filename(Upload_File.filename)))
		
		# files = request.files.getlist("Upload_File")
		# for file in files:
		# 	print(file.filename)
		# 	file.save(join(user_folder, secure_filename(file.filename)))

		return redirect(url_for("page2"),)
	return render_template("page1.html")




# response = requests.get(f"   {username}")
# response = requests.delete(f"   {username}")
#  response = requests.post("", json = emp , headers = headers )
#  response = requests.put(f"   {id}", json = emp , headers = headers )



@app.route("/page2" , methods = ['GET','POST'])
def page2():
	
	if request.method == "POST":
		print(request.form.get("Customise", False))
		Duplexity_spec = request.form.get("p2_ds", False)
		Color_spec = request.form.get("p2_cs", False)
		Size_spec = request.form.get("p2_ss", False)
		Binding = request.form.get("p2_bs", False)
		G_loc = request.form.get("p2_mloc", False)
		Address = request.form.get("p2_addr", False)

		Customise = request.form.get("Customise", False)
		print(Customise)
		if Customise != "Customise":
			return render_template("goodbye.html", enquiry = Customise)




		print(Duplexity_spec, Color_spec, Size_spec,  Binding, G_loc , Address)
		# return redirect(url_for("page3"))
		return render_template("page3.html")

	return render_template("page2.html")

# @app.route("/page3")
# def page3():
# 	print("hrllo")
# 	return render_template("page3.html")



@app.route("/goodbye")
def goodbye():
	print("hrllo")
	return render_template("goodbye.html")


app.run(debug=True)


# {"Page": "page1", "response_time": 0.10043787956237793, "C_id": "1", "O_id": "1", "api_request_status": "Successful"}
# {"Page": "page2", "response_time": 0.03404521942138672, "checkout_msg": "", "final_price": {"no_of_BW_pages": 0, "CPP_BW": 0, "cost_BW_pages": 0, "no_of_color_pages": 0, "CPP_color": 0, "cost_color_pages": 0, "binding_cost_per_copy": 0, "cost_per_copy": 0, "no_of_copies": 1, "delivery_cost": 0, "total_cost": 0}, "api_request_status": "Successful"}

