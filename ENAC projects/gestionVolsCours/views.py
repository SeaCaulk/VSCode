from flask import Flask, render_template, redirect, url_for, request
import os
import json

def load():
  if os.path.getsize("ENAC projects/gestionVolsCours/flights.txt")>0:
    with open("ENAC projects/gestionVolsCours/flights.txt", "r") as file:
        flights = json.load(file)
  else:
    flights = []
  return(flights)
def dump(l):
  flights=load()
  flights.append(l)
  with open("ENAC projects/gestionVolsCours/flights.txt", "w") as file:
    json.dump(flights,file)
app = Flask(__name__)

app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('config')

#page d'accueil
@app.route("/")
def index():
  return render_template("index.html", flights=load())

@app.route("/ajouter", methods=["POST", "GET"])
def ajouter():
  if request.method == "POST":
    dump([request.form["indicatif"], request.form["OACIDep"], request.form["OACIArr"], request.form["Hdep"], request.form["Harr"]])
  return render_template("ajouter.html", flights=load())

@app.route("/modifier", methods=["POST","GET"])
def modifier():
  if request.method=="POST":
    flights=load()
    flights[int(request.form["current"])]=[request.form["indicatif"], request.form["OACIDep"], request.form["OACIArr"], request.form["Hdep"], request.form["Harr"]]
    print(flights[int(request.form["current"])])
    with open("ENAC projects/gestionVolsCours/flights.txt", "w") as file:
      json.dump(flights,file)
  return render_template("modifier.html", flights=load(), current=-1)
@app.route("/modifier[<int:id>]")
def modifId(id):
  return render_template("modifier.html", flights=load(), current=id)

@app.route("/supprimer")
def supprimer():
  return render_template("supprimer.html", flights=load())

@app.route("/connecter")
def connecter():
  return render_template("connecter.html")

@app.route("/afficher")
def afficher():
  return redirect(url_for('index', _anchor='vols'))
