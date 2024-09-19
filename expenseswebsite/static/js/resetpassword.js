const passwordField = document.querySelector('#passwordField');
const confirmPasswordField = document.querySelector('#confirmPasswordField');
const showPassword = document.querySelectorAll('.showPassword');
const submitBtn = document.querySelector('.submit-btn');

let passwordValid = false;
let passwordsMatch = false;


function validatePassword(password) {
    const minLength = 8;
    const hasNumbers = /\d/;
    const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/;

    return password.length >= minLength && hasNumbers.test(password) && hasSpecialChars.test(password);
}


function toggleSubmitButton() {
    if (passwordValid && passwordsMatch) {
        submitBtn.removeAttribute('disabled');
    } else {
        submitBtn.setAttribute('disabled', 'disabled');
    }
}

passwordField?.addEventListener('keyup', (e) => {
    const passwordVal = e.target.value;
    passwordValid = validatePassword(passwordVal);

    if (passwordValid) {
        passwordField.classList.remove('is-invalid');
        passwordField.classList.add('is-valid');
    } else {
        passwordField.classList.add('is-invalid');
        passwordField.classList.remove('is-valid');
    }
    checkPasswordsMatch();
    toggleSubmitButton();
});


confirmPasswordField?.addEventListener('keyup', (e) => {
    checkPasswordsMatch();
    toggleSubmitButton();
});


function checkPasswordsMatch() {
    if (passwordField.value === confirmPasswordField.value && passwordField.value !== "") {
        confirmPasswordField.classList.add('is-valid');
        confirmPasswordField.classList.remove('is-invalid');
        passwordsMatch = true;
    } else {
        confirmPasswordField.classList.add('is-invalid');
        confirmPasswordField.classList.remove('is-valid');
        passwordsMatch = false;
    }
}


showPassword?.forEach((toggleBtn) => {
    toggleBtn.addEventListener('click', (e) => {
        const passwordInput = e.target.previousElementSibling;
        if (toggleBtn.textContent === 'Show') {
            toggleBtn.textContent = 'Hide';
            passwordInput.setAttribute('type', 'text');
        } else {
            toggleBtn.textContent = 'Show';
            passwordInput.setAttribute('type', 'password');
        }
    });
});


toggleSubmitButton();
