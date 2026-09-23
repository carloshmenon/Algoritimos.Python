<?php $title_page = "Usuários"; 
$menuSection = "usuarios";?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hospital São julião</title>
    <link rel="stylesheet" href="../css/styles.css" />
    <link rel="stylesheet" href="../css/header.css" />
    <link rel="stylesheet" href="../css/aside.css" />
    <link rel="stylesheet" href="../css/main.css" />
    <link rel="stylesheet" href="../css/usuarios-listagem.css" />
</head>
<body>
    <?php require __DIR__ . '/sidebar.php'; ?>

    <section class="container-main">
        <?php require __DIR__ . '/topbar.php'; ?>

        <main class="main-content">
            <div class="container-principal-usuarios-listagem">

                <table-padrao
                    id="tabela-usuarios-listagem"
                    nome="Usuarios"
                    url="../services/usuarios-listagem-dados.php"
                    tamanhoPag="10"
                    temPesquisa
                    adicionar
                    selecionar
                    editar
                ></table-padrao>

            </div>
        </main>
    </section>

    <script src="../js/components/btn-padrao.js"></script>
    <script src="../js/components/table-component.js"></script>
    <script src="../js/pages/usuarios-listagem.js"></script>
</body>
</html>
