from flask import Flask
from views import views

app = Flask(__name__) #creating the 'app' object from the class 'Flask'
app.register_blueprint(views) #register the views blueprint

if __name__ == "__main__":
    app.run(debug=True, port=8000) #running the application

