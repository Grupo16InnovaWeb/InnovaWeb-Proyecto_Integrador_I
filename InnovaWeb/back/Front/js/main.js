// Validación de Login
const loginForm = document.getElementById("loginForm");
if (loginForm) {
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const msg = document.getElementById("loginMsg");

    if (email === "admin@innovaweb.com" && password === "12345") {
      msg.innerHTML = "<p class='text-success'>Inicio de sesión exitoso. Redirigiendo...</p>";
      setTimeout(() => {
        window.location.href = "index.html";
      }, 1500);
    } else {
      msg.innerHTML = "<p class='text-danger'>Usuario o contraseña incorrectos.</p>";
    }
  });
}

// Validación de Registro
const registroForm = document.getElementById("registroForm");
if (registroForm) {
  registroForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const password = document.getElementById("password").value;
    const confirm = document.getElementById("confirmPassword").value;
    const msg = document.getElementById("registroMsg");

    if (password !== confirm) {
      msg.innerHTML = "<p class='text-danger'>Las contraseñas no coinciden.</p>";
    } else {
      msg.innerHTML = "<p class='text-success'>Registro exitoso. Redirigiendo al login...</p>";
      setTimeout(() => {
        window.location.href = "login.html";
      }, 1500);
    }
  });
}
