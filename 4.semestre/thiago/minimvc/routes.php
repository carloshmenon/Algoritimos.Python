<?php

use miniMVC\Controller\UsuarioController;

$url = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);


// echo $url;

switch($url)
{
    case '/minimvc/usuario':
        // echo "CHAMAR A CLASSE DE USUARIO";
        UsuarioController::all();
    break;

    case '/minimvc/veiculo':
        echo "CHAMAR A CLASSE DE VEICULO";
    break;
}