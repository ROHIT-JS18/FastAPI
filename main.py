import json
from fastapi import FastAPI
app = FastAPI()

# Define a route and a function (e.g., a "Hello World" endpoint):
# python

def load_data():
    with open('patient.json' , 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return 

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()

    return data