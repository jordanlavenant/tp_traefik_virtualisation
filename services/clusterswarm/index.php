<?php
    $server_ip = $_SERVER['SERVER_ADDR'];
    // Nom d'hôte du serveur
    $server_host = gethostname();

    echo "<html><head></head><body>";
    echo "Adresse IP du serveur docker : $server_ip<br>";
    echo "Nom d'hôte du serveur docker : $server_host<br>";
?>