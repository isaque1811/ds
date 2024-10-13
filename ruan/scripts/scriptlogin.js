document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Aqui você pode adicionar sua lógica de autenticação
    alert(`Usuário: ${username}\nSenha: ${password}`);
      // Redireciona para a página de sucesso ou outra página
      window.location.href = 'pagina.html'; // Altere para o nome da sua página
});
