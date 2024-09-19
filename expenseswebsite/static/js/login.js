document.addEventListener('DOMContentLoaded', function () {
    const passwordField = document.querySelector('#passwordField');
    const showPassword = document.querySelector('.showPassword');

    showPassword.addEventListener('click', () => {
        if (showPassword.textContent === 'Show') {
            showPassword.textContent = 'Hide';
            passwordField.setAttribute('type', 'text');
        } else {
            showPassword.textContent = 'Show';
            passwordField.setAttribute('type', 'password');
        }
    });
});
