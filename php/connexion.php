<?php

$connexion= new mysqli("localhost","root","josue2005","projetagl2");

if ($connexion->connect_error) {
    die("La connexion à la base de données a échoué : " . $connexion->connect_error);
}

$pseudo=$_POST['pseudo'];
$mp=$_POST['pwd'];

$sql = "SELECT * FROM user WHERE pseudo = '$pseudo' AND mp = '$mp'";
$result = $connexion->query($sql);

// Vérifier si des résultats ont été trouvés
if ($result->num_rows > 0) {
    header("Location: ../html/categorie.html");
    exit();
} else {
    // Les informations sont incorrectes, l'utilisateur n'est pas authentifié
    echo "Authentification échouée. Vérifiez vos informations.";
}



?>