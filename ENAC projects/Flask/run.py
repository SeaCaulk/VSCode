from flask import Flask,render_template

app = Flask(__name__)

@app.route ('/')
def index ():
    return render_template('index.html')
@app.route ( "/page2" )
def page2() :
    return " Contenu page2 "
@app.route ( "/page3" )
def page3() :
    print (" affichage dans console ")
    return " Contenu page3"
@app.route("/webmaster") 
def webmaster() :
      return ' page décrivant le ' \
    '<strong>webmaster</strong> ' \
    'avec son meilleur profil : ' \
    ' <img src = " /static/images/image01.jpg " >'
    
if __name__=='__main__':
    # app.run(debug='True') #mode developpement
    app.run(debug=False,host='0.0.0.0') #en mode production (ip a pour récupérer l adresse de la machine)
