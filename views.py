from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

#views is a blueprint

task_list = []

@views.route("/") #route the homepage
def home():
    return render_template("index.html")

@views.route("/contact") #route the contact page
def contact():
    return render_template("contact.html")

@views.route("/about") #route the about page
def about():
    return render_template("about.html")

@views.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method == "POST": #if method is post
        task = request.form.get ("task-input") #get the input
        task_list.append(task) #add to list
        print(task_list)
        return render_template("todos.html", task_list = task_list) #return page with appended list
    return render_template("todos.html") #else show page without list
