document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Aqui você pode adicionar sua lógica de cadastro
    alert(`Usuário: ${username}\nEmail: ${email}\nSenha: ${password}`);

    // Redireciona para a página de sucesso ou outra página
    window.location.href = 'login.html'; // Altere para o nome da sua página
});
