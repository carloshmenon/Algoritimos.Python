document.addEventListener("DOMContentLoaded", () => {
    const tabela = document.getElementById("tabela-usuarios-listagem");

    if (!tabela) return;

    tabela.addEventListener("adicionar", () => {
        window.location.href = "usuarios-cadastro.php";
    });

    tabela.addEventListener("selecionar", (event) => {
        const { id } = event.detail;
        window.location.href = `usuarios-visualizar.php?id=${id}`;
    });

    tabela.addEventListener("editar", (event) => {
        const { id } = event.detail;
        window.location.href = `usuarios-editar.php?id=${id}`;
    });
});
