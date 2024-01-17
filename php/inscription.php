<?php

$connexion= new mysqli("localhost","root","josue2005","projetagl2");

if ($connexion->connect_error) {
    die("La connexion à la base de données a échoué : " . $connexion->connect_error);
}

$nom=$_POST['nom'];
$prenom=$_POST['prenom'];
$pseudo=$_POST['pseudo'];
$email=$_POST['email'];
$mp=$_POST['pwd'];


$requete="INSERT INTO user(nom,prenom,pseudo,email,mp) VALUES ('$nom','$prenom','$pseudo','$email','$mp')";

if ($connexion->query($requete) === TRUE) {
    echo "Enregistrement réussi !";
} else {
    echo "Erreur lors de l'enregistrement : " . $connexion->error;
}


?>