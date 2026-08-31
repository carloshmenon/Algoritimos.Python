<?php

namespace miniMVC\DAO;

use miniMVC\Model\UsuarioModel;

class UsuarioDAO extends DAO
{
    public function __construct()
    {
        parent::__construct();
    }

    public function select() : array
    {
        $sql = "SELECT * FROM usuario";
        $stmt = parent::$connection->prepare($sql);
        $stmt->execute();

        return $stmt->fetchAll(DAO::FETCH_CLASS, "miniMVC\Model\UsuarioModel");
    }
}

?>