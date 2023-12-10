// JavaScript for handling form submission
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting

        // Your form validation and submission logic here

        // Assuming the form is successfully submitted:
        localStorage.setItem('formSubmitted', 'true');

        // Redirect to the "Thank You" page
        window.location.href = 'thank_you.html';
    });

    // Check if the "formSubmitted" flag is set in local storage
    const formSubmitted = localStorage.getItem('formSubmitted');
    if (formSubmitted === 'true') {
        // If the form was previously submitted, redirect to the "Thank You" page
        window.location.href = 'thank_you.html';
    }
});

// JavaScript for handling form submission and redirection
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting

        // Your form validation and submission logic here

        // Assuming the form is successfully submitted:
        localStorage.setItem('formSubmitted', 'true');

        // Redirect to the "Thank You" page
        window.location.href = 'thank_you.html';
    });

    // Check if the "formSubmitted" flag is set in local storage
    const formSubmitted = localStorage.getItem('formSubmitted');
    if (formSubmitted !== 'true') {
        // If the form was not previously submitted, redirect to the "Create Request" page
        window.location.href = 'create_request.html';
    }
});
