document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('contactButton').addEventListener('click', function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            alert("Todos los campos son obligatorios.");
            return;
        }

        const mailtoLink = 'mailto:orlibet@gmail.com' +
            '?subject=' + encodeURIComponent('Nuevo mensaje de contacto') +
            '&body=' + encodeURIComponent('Nombre: ' + name + '\nEmail: ' + email + '\n\nMensaje:\n' + message);

        window.location.href = mailtoLink;

        document.getElementById('name').value = '';
        document.getElementById('email').value = '';
        document.getElementById('message').value = '';
    })
});