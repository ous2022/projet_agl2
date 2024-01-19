from flask import Flask,render_template,request,redirect,flash,url_for,session
#redirect permet de renvoyer une url
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash



app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete_unique_et_securisee'


#configurer la bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db = SQLAlchemy(app)

#creation de la bd
class Utilisateur(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nom = db.Column(db.String(150),nullable=False)
    prenom = db.Column(db.String(150),nullable=False)
    nom_utilisateur = db.Column(db.String(20),unique=True,nullable=False) 
    email = db.Column(db.String(120),unique=True,nullable=False) 
    mot_de_passe = db.Column(db.String(40),nullable=False) 


# #supprimer les elements des colonnes
# Utilisateur.query.delete()
# db.session.commit()


# commandes a taper dans le terminal pour creer la bd
# - from app import db
# - db.create_all()


#afficher valeurs bd
def __repr__(self):
        return f"utilisateur[{self.id}, {self.nom},{self.prenom},{self.nom_utilisateur},{self.email},{self.mot_de_passe}]"
    

#urls
@app.route("/")
def page_de_garde():
    return render_template("page_de_garde.html")

@app.route("/accueil")
def accueil():
    return render_template("page_acceuil.html")

@app.route("/categories")
def categories():
    return render_template("categorie.html")

#produit prescolaire
@app.route("/prescolaire")
def prescolaire():
    return render_template("page_produit_préscolaire.html")

@app.route("/prescolaire/detail_cahier_coloriage")
def detail_cc():
    return render_template("detail_cahier_coloriage.html")

@app.route("/prescolaire/gomme")
def gomme():
    return render_template("detail_gomme.html")

@app.route("/prescolaire/cahier_dessin")
def dessin():
    return render_template("detail_cahier_dessin.html")

@app.route("/prescolaire/gourde")
def gourde():
    return render_template("detail_gourde.html")

@app.route("/prescolaire/boite_gouter")
def boite_gouter():
    return render_template("detail_boite_gouter.html")

@app.route("/prescolaire/livre_histoire")
def livre_histoire():
    return render_template("detail_livre_histoire.html")

@app.route("/prescolaire/crayon_couleurs")
def crayon_couleurs():
    return render_template("detail_crayon_couleurs.html")

@app.route("/prescolaire/ciseau")
def ciseau():
    return render_template("detail_ciseau.html")

@app.route("/prescolaire/colle")
def colle():
    return render_template("detail_colle.html")

@app.route("/prescolaire/crayon")
def crayon():
    return render_template("detail_crayon_papier.html")

@app.route("/prescolaire/feutre")
def feutre():
    return render_template("detail_feutre.html")

@app.route("/prescolaire/papier_carton")
def papier_carton():
    return render_template("detail_papier_carton.html")

@app.route("/prescolaire/tablier")
def tablier():
    return render_template("detail_tablier.html")

#produit primaire
@app.route("/primaire")
def prescolaireP():
    return render_template("page_produit_primaire.html")

@app.route("/primaire/detail_cahier_coloriage")
def detail_ccP():
    return render_template("detail_cahier_coloriage.html")

@app.route("/primaire/gomme")
def gommeP():
    return render_template("detail_gomme.html")

@app.route("/primaire/cahier_dessin")
def dessinP():
    return render_template("detail_cahier_dessin.html")

@app.route("/primaire/gourde")
def gourdeP():
    return render_template("detail_gourde.html")

@app.route("/primaire/boite_gouter")
def boite_gouterP():
    return render_template("detail_boite_gouter.html")

@app.route("/primaire/livre_histoire")
def livre_histoireP():
    return render_template("detail_livre_histoire.html")

@app.route("/primaire/crayon_couleurs")
def crayon_couleursP():
    return render_template("detail_crayon_couleurs.html")

@app.route("/primaire/ciseau")
def ciseauP():
    return render_template("detail_ciseau.html")

@app.route("/primaire/colle")
def colleP():
    return render_template("detail_colle.html")

@app.route("/primaire/crayon")
def crayonP():
    return render_template("detail_crayon_papier.html")

@app.route("/primaire/feutre")
def feutreP():
    return render_template("detail_feutre.html")

@app.route("/primaire/papier_carton")
def papier_cartonP():
    return render_template("detail_papier_carton.html")

@app.route("/primaire/tablier")
def tablierP():
    return render_template("detail_tablier.html")

#produit lycee
@app.route("/lycee")
def prescolaireL():
    return render_template("page_produit_préscolaire.html")

@app.route("/lycee/detail_cahier_coloriage")
def detail_ccL():
    return render_template("detail_cahier_coloriage.html")

@app.route("/lycee/gomme")
def gommeL():
    return render_template("detail_gomme.html")

@app.route("/lycee/cahier_dessin")
def dessinL():
    return render_template("detail_cahier_dessin.html")

@app.route("/lycee/gourde")
def gourdeL():
    return render_template("detail_gourde.html")

@app.route("/lycee/boite_gouter")
def boite_gouterL():
    return render_template("detail_boite_gouter.html")

@app.route("/lycee/livre_histoire")
def livre_histoireL():
    return render_template("detail_livre_histoire.html")

@app.route("/lycee/crayon_couleurs")
def crayon_couleursL():
    return render_template("detail_crayon_couleurs.html")

@app.route("/lycee/ciseau")
def ciseauL():
    return render_template("detail_ciseau.html")

@app.route("/lycee/colle")
def colleL():
    return render_template("detail_colle.html")

@app.route("/lycee/crayon")
def crayonL():
    return render_template("detail_crayon_papier.html")

@app.route("/lycee/feutre")
def feutreL():
    return render_template("detail_feutre.html")

@app.route("/lycee/papier_carton")
def papier_cartonL():
    return render_template("detail_papier_carton.html")

@app.route("/lycee/tablier")
def tablierL():
    return render_template("detail_tablier.html")

#produit college
@app.route("/college")
def prescolaireC():
    return render_template("page_produit_préscolaire.html")

@app.route("/college/detail_cahier_coloriage")
def detail_ccC():
    return render_template("detail_cahier_coloriage.html")

@app.route("/college/gomme")
def gommeC():
    return render_template("detail_gomme.html")

@app.route("/college/cahier_dessin")
def dessinC():
    return render_template("detail_cahier_dessin.html")

@app.route("/college/gourde")
def gourdeC():
    return render_template("detail_gourde.html")

@app.route("/college/boite_gouter")
def boite_gouterC():
    return render_template("detail_boite_gouter.html")

@app.route("/college/livre_histoire")
def livre_histoireC():
    return render_template("detail_livre_histoire.html")

@app.route("/college/crayon_couleurs")
def crayon_couleursC():
    return render_template("detail_crayon_couleurs.html")

@app.route("/college/ciseau")
def ciseauC():
    return render_template("detail_ciseau.html")

@app.route("/college/colle")
def colleC():
    return render_template("detail_colle.html")

@app.route("/college/crayon")
def crayonC():
    return render_template("detail_crayon_papier.html")

@app.route("/college/feutre")
def feutreC():
    return render_template("detail_feutre.html")

@app.route("/college/papier_carton")
def papier_cartonC():
    return render_template("detail_papier_carton.html")

@app.route("/college/tablier")
def tablierC():
    return render_template("detail_tablier.html")

#recuperer donnees form

@app.route("/connexion", methods=["GET","POST"])
def connexion():
    if request.method == "POST":
        nom_utilisateur = request.form.get('name')
        mot_de_passe = request.form.get('pwd')

        # Recherche de l'utilisateur dans la base de données
        utilisateur = Utilisateur.query.filter_by(nom_utilisateur=nom_utilisateur).first()

        if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe):
            # Connexion réussie
            flash('Connexion réussie!', 'success')

            # Stocker les informations de l'utilisateur dans la session
            session['utilisateur_id'] = utilisateur.id
            session['nom_utilisateur'] = utilisateur.nom_utilisateur
            session['email'] = utilisateur.email

            # Redirection vers une autre page ou effectuer d'autres actions
            return redirect(url_for('page_de_garde'))
        else:
            # Échec de la connexion
            flash('Le nom d\'utilisateur ou le mot de passe est incorrect. Veuillez réessayer.', 'error')

    return render_template("page_connexion.html")

@app.route("/inscription",methods=["GET","POST"])
def inscription():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']

        #hasher le mp avant de l'enregistrer dans la bd
        pwd_hash = generate_password_hash(pwd, method='sha256')
        nouvel_utilisateur = Utilisateur(nom=nom, prenom=prenom, nom_utilisateur=name, email=email, mot_de_passe=pwd_hash)

        db.session.add(nouvel_utilisateur)
        db.session.commit()

        #enregistrer un message flash pour afficher après la redirection
        flash('Connectez-vous maintenant!','success')

        #rediriger vers la page de connexion
        return redirect(url_for('accueil'))
    
        
    return render_template("page_inscription.html")


#panier 
@app.route("/panier")
def panier():
    # Récupérer les informations du panier (exemple)
    panier = [
        {"produit": "Cahier", "quantite": 2, "prix_unitaire": 5.99},
        {"produit": "Stylo", "quantite": 3, "prix_unitaire": 2.49},
        # Ajoutez d'autres produits du panier ici
    ]

    montant_total = sum(item["quantite"] * item["prix_unitaire"] for item in panier)

    return render_template("panier.html", panier=panier, montant_total=montant_total)
