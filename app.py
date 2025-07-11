from flask import Flask, render_template, request, redirect, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = "shhh_luffy_secret"
app.config['AMMMMMM'] = "shellmates{SA7AAAAAAAAAAAAAAAAAAAA}"

todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        session["name"] = name
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "name" not in session:
        return redirect("/")

    if request.method == "POST":
        title = request.form.get("title")  
        description = request.form.get("description")

        todos.append({"title": title, "description": description}) 

    name = session.get("name", "Luffy")
    rendered_welcome = render_template_string("Welcome " + name)  

    return render_template("dashboard.html", todos=todos, welcome_message=rendered_welcome)

@app.route("/logout")
def logout():
    session.clear()
    todos.clear()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
