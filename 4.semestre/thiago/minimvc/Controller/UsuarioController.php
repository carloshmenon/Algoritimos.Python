<?php

namespace miniMVC\Controller;

use miniMVC\Model\UsuarioModel;

class UsuarioController
{

    public static function all()
    {
        $usuarios = UsuarioModel::getAllRows();
        include VIEW . '/usuario/listar_usuarios.php';
    }
}

