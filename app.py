from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {"id": 1, "title": "clean your house", "done": False},
    {"id": 2, "title": "do your tp flask", "done": True},
    {"id": 3, "title": "go to casablanca", "done": False}
]

id = 3
@app.get("/")
def home():
    return render_template("index.html", todos=todos)

@app.post("/add")
def add_todo():
    global id
    title = request.form.get("title")

    if title:
        id += 1  # unique ID
        todos.append({
            "id": id,
            "title": title,
            "done": False
        })

    return redirect(url_for("home"))

@app.get("/terminer/<int:task_id>")
def terminer(task_id):
    for t in todos:
        if t["id"] == task_id:
            t["done"] = True
            break
    return redirect(url_for("home"))

@app.get("/delete/<int:task_id>")
def delete(task_id):
    for t in todos:
        if t["id"] == task_id:
            todos.remove(t)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
