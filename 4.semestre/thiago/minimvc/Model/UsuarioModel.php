<?php

namespace miniMVC\Model;

use miniMVC\DAO\UsuarioDAO;

class UsuarioModel
{
    public ?int $id_usuario;
    public string $nome;
    public string $email;
    public string $senha;
    public string $tipo;

    public static function getAllRows()
    {
        $objUsers = new UsuarioDAO();
        return $objUsers->select();
    }

    public static function getById()
    {
        
    }

    public static function save()
    {
        
    }
}