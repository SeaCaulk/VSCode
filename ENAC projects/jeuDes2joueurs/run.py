from flask import Flask,render_template,request,session,redirect
import mesfonctions

app = Flask(__name__)
app.secret_key="azerty"
PARTIE ="./data/partie.txt"

@app.route('/') # page d'accueil
def index():
    return render_template("index.html")

@app.route('/connecter') #page permettant de selectionner son joueur
def connecter():
    return render_template("connecter.html")

@app.route('/login',methods=['POST'])   #route qui mémorise le numéro du joueur dans la session puis qui débute la partie directement
def login():
    session["no_joueur"] = int(request.form["no_joueur"])   #la valeur du joueur est soit 0 soit 1 cf connecter.html
    if session['no_joueur']== 0 :
        mesfonctions.init(PARTIE,session['no_joueur'])
    return redirect('/jouer')
 
@app.route('/logout',methods=['POST'])  #route de déconnexion
def deconnecter():
    session.clear()
    return redirect('/connecter')

@app.route('/jouer') #route faisant jouer un tour pour un joueur, le joueur courant
def jouer():
    partie = mesfonctions.charger_partie(PARTIE)
   
    if partie['joueur_courant']==session['no_joueur']:
        mesfonctions.jouer_tour(partie)
        mesfonctions.sauver_partie(partie,PARTIE)
    else:
        return render_template("jouer.html",partie=partie,mess = "C'est pas à toi !!!")
    return render_template("jouer.html",partie=partie)

if __name__ == '__main__':
    app.run(debug=True)
