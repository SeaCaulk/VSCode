from flask import Flask, render_template, redirect, url_for, request
import os
import json
import jeu

# def load():
#   if os.path.getsize("ENAC projects/gestionVolsCours/flights.txt")>0:
#     with open("ENAC projects/gestionVolsCours/flights.txt", "r") as file:
#         flights = json.load(file)
#   else:
#     flights = []
#   return(flights)
# def laod():
#   if os.path.getsize("ENAC projects/gestionVolsCours/aircrafts.txt")>0:
#     with open("ENAC projects/gestionVolsCours/aircrafts.txt", "r") as file:
#         aircrafts = json.load(file)
#   else:
#     aircrafts = []
#   return(aircrafts)
# def dump(l):
#   flights=load()
#   flights.append(l)
#   with open("ENAC projects/gestionVolsCours/flights.txt", "w") as file:
#     json.dump(flights,file)
# def dmup(l):
#   flights=laod()
#   flights.append(l)
#   with open("ENAC projects/gestionVolsCours/aircrafts.txt", "w") as file:
#     json.dump(flights,file)

app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('config')

#page d'accueil
@app.route("/")
def index():
  return render_template("index.html")

#page des règles
@app.route("/rules")
def rules():
  return render_template("rules.html")

#page du jeu lui-même
@app.route("/game", methods=["GET", "POST"])
def game():
  if request.method=="POST":
    jeu.tour(request.form["joueur"],jeu.cartes,request.form["input"],jeu.R,jeu.K,request.form["input2"],request.form["inputlists"])
  return render_template("game.html", cartesPosees=jeu.cartesPosees,joueurs=jeu.Joueurs, scores=jeu.scores,cartes=jeu.cartes,R=jeu.R,K=jeu.K)