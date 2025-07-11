from flask import Flask, render_template, request, redirect, session, render_template_string

app = Flask(__name__)
app.secret_key = "shhh_luffy_secret"

# Config-hidden flags
app.config['FLAG1'] = "CTF{first_part_hidden_in_config_"
app.config['FLAG2'] = "second_part_hidden_in_config}"

# In-memory todo list
todos = []

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        session["user"] = username
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        title = request.form.get("title")  # VULNERABLE
        description = request.form.get("description")

        # Vulnerable SSTI rendering
        rendered_title = render_template_string(title)
        todos.append({"title": rendered_title, "description": description})

    return render_template("dashboard.html", todos=todos, user=session["user"], config=app.config)

@app.route("/logout")
def logout():
    session.clear()
    todos.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
