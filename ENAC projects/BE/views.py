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
    jeu.init(['J1'])
  action=request.form.get("action")
  selected_cards=request.form.getlist("selected_cards")
  if action==None:
    pass
  elif action[:4]=="take":
    jeu.take(Id,action)
  elif action=="pose":
    if jeu.pose(selected_cards,Id)==True:
      id-=1

  elif action=="give":
    if len(selected_cards)>1:
      id-=1
    else:
      try :
        jeu.give(Id,selected_cards[0])
      except:
        id-=1



  return render_template("game.html",player=Id, cartesPosees=jeu.cartesPosees,Joueurs=jeu.Joueurs, scores=jeu.scores,cartes=jeu.cartes,R=jeu.R,K=jeu.K,word=d,id=id,J1='J1',J2='J2')

  # if Id=="pose":
  #   if request.method=="POST":
  #     jeu.pose(request.form["cartes"])
  # elif Id[:4]=="take":
  #   print('success')
  #   jeu.take('J1',Id)
  # elif Id=="give":
  #   if request.method=="POST":
  #     jeu.give('J1',request.form["carte"])



  # if id==3:
  #   if d=='B':
  #     playerlist=['J1']
  #   else:
  #     playerlist=['J1','J2']
  #   jeu.init(playerlist)
  # if Id=="give" and id==1:
  #   if request.method=="POST":
  #     jeu.give(request.form["carte"],request.form["joueur"])
  # elif id==2:
  #   pass
  # elif Id=="pose":
  #   if request.method=="POST":
  #     jeu.pose(jeu.cartesPosees,request.form["cartes"])
  # elif id==1:
  #   pass
  # elif Id=="take":
  #   if request.method=="POST":
  #     jeu.take("joueur1",jeu.Joueurs,request.form["input"],jeu.R,jeu.K)
