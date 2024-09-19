const usernameField=document.querySelector('#usernameField');
const feedbackArea=document.querySelector('.invalid-feedback')
const emailField=document.querySelector('#emailField')
const emailFeedbackArea = document.querySelector('.emailFeedbackArea'); 
const passwordField = document.querySelector('#passwordField')
const showPassword=document.querySelector('.showPassword')
const submitBtn=document.querySelector('.submit-btn')

let usernameValid = false;
let emailValid = false;
let passwordValid = false;

function validatePassword(password) {
    const minLength = 8;
    const hasNumbers = /\d/;
    const hasSpecialChars = /[!@#$%^&*(),.?":{}|<>]/;

    return password.length >= minLength && hasNumbers.test(password) && hasSpecialChars.test(password);
}

function toggleSubmitButton() {
    if (usernameValid && emailValid && passwordValid) {
        submitBtn.removeAttribute('disabled');
    } else {
        submitBtn.setAttribute('disabled', 'disabled');
    }
}

/*function checkFormValidity() {
    if (usernameField.classList.contains('is-valid') && emailField.classList.contains('is-valid')) {
        submitBtn.removeAttribute('disabled');
    } else {
        submitBtn.setAttribute('disabled', 'disabled');
    }
}*/

usernameField.addEventListener('keyup',(e)=>{ //'key up' as sommeone is typing
    console.log('it"s up');

    const usernameVal=e.target.value; /*gets the username*/
    /*console.log(usernameVal);*/

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('Username:', usernameVal, 'Response:', data);
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                usernameField.classList.remove('is-valid');
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                usernameValid = false;
            } else {
                usernameField.classList.remove('is-invalid');
                usernameField.classList.add('is-valid');
                feedbackArea.style.display = 'none';
                usernameValid = true;
            }
            //checkFormValidity(); 
            toggleSubmitButton(); 
        });
    } else {
        usernameField.classList.remove('is-invalid');
        usernameField.classList.remove('is-valid');
        feedbackArea.style.display = 'none';
        console.log('Username is empty');
        usernameValid = false;
        toggleSubmitButton(); 
    }
    
});

emailField.addEventListener('keyup',(e)=>{ //'key up' as sommeone is typing
    console.log('it"s up too');

    const emailVal=e.target.value; /*gets the email*/
    /*console.log(usernameVal);*/
    emailFeedbackArea.style.display='none';

    if (emailVal.length > 0) {
        fetch('/authentication/validate-email', {
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('email:', emailVal, 'Response:', data);
            if (data.email_error) {
                emailField.classList.add('is-invalid');
                emailField.classList.remove('is-valid'); 
                emailFeedbackArea.style.display = 'block';
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
                emailValid = false;
            } else {
                emailField.classList.remove('is-invalid');
                emailField.classList.add('is-valid');
                feedbackArea.style.display = 'none';
                emailValid = true;
            }
            //checkFormValidity(); 
            toggleSubmitButton();
        });
    } else {
        emailField.classList.remove('is-invalid');
        emailField.classList.remove('is-valid'); 
        feedbackArea.style.display = 'none';
        console.log('Email is empty');
        //checkFormValidity(); 
        emailValid = false;
        toggleSubmitButton();
    }
});

passwordField.addEventListener('keyup', (e) => {
    const passwordVal = e.target.value;
    passwordValid = validatePassword(passwordVal);

    if (passwordValid) {
        passwordField.classList.remove('is-invalid');
        passwordField.classList.add('is-valid');
    } else {
        passwordField.classList.add('is-invalid');
        passwordField.classList.remove('is-valid');
    }
    toggleSubmitButton();
});

showPassword.addEventListener('click',(e)=>{

    if (showPassword.textContent==='Show'){
        showPassword.textContent='Hide'
        passwordField.setAttribute('type','text')

    }else{showPassword.textContent='Show';passwordField.setAttribute('type','password')}

});

//btn disabled before running 'check'
//submitBtn.setAttribute('disabled', 'disabled');
toggleSubmitButton();

console.log('register ok!');









console.log('register ok!')