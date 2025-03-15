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
@app.route("/game<string:d>[<int:id>,<string:Id>]", methods=["GET", "POST"])
def game(d,id,Id):
  if id==3:
    if d=='B':
      playerlist=['J1']
    else:
      playerlist=['J1','J2']
    jeu.init(playerlist)
  if Id=="give" and id==1:
    if request.method=="POST":
      jeu.give(request.form["carte"],request.form["joueur"])
  elif id==2:
    pass
  elif Id=="pose":
    if request.method=="POST":
      jeu.pose(jeu.cartesPosees,request.form["cartes"])
  elif id==1:
    pass
  elif Id=="take":
    if request.method=="POST":
      jeu.take("joueur1",jeu.Joueurs,request.form["input"],jeu.R,jeu.K)

  return render_template("game.html", cartesPosees=jeu.cartesPosees,Joueurs=jeu.Joueurs, scores=jeu.scores,cartes=jeu.cartes,R=jeu.R,K=jeu.K,word=d,J1='J1',J2='J2')