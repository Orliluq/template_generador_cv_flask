document.addEventListener('DOMContentLoaded', () => {
  const contactButton = document.getElementById('contactButton');
  if (!contactButton) return;

  contactButton.addEventListener('click', (event) => {
    event.preventDefault();

    const name = document.getElementById('name')?.value.trim();
    const email = document.getElementById('email')?.value.trim();
    const message = document.getElementById('message')?.value.trim();

    if (!name || !email || !message) {
      alert("Todos los campos son obligatorios.");
      return;
    }

    const subject = encodeURIComponent('Nuevo mensaje de contacto');
    const body = encodeURIComponent(`Nombre: ${name}\nEmail: ${email}\n\nMensaje:\n${message}`);
    window.location.href = `mailto:example@gmail.com?subject=${subject}&body=${body}`;

    // Limpiar formulario
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('message').value = '';
  });
});