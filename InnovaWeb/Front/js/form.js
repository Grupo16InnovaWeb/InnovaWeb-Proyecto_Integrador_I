(function () {
  'use strict'
  const form = document.getElementById('contactForm');
  const feedbackDiv = document.getElementById('formFeedback');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopPropagation();

    if (!form.checkValidity()) {
      form.classList.add('was-validated');
      feedbackDiv.textContent = '';
      return;
    }

    feedbackDiv.textContent = 'Mensaje enviado correctamente. ¡Gracias!';
    feedbackDiv.classList.remove('text-danger');
    feedbackDiv.classList.add('text-success');

    form.reset();
    form.classList.remove('was-validated');
  }, false);
})();
