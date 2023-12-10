const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

signupBtn.onclick = (() => {
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";

  // Show additional fields for sign-up
  document.querySelectorAll(".signup .field").forEach((field) => {
    field.style.display = "block";
  });
});

loginBtn.onclick = (() => {
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";

  // Hide additional fields for sign-up
  document.querySelectorAll(".signup .field").forEach((field) => {
    field.style.display = "none";
  });
});

signupLink.onclick = (() => {
  signupBtn.click();
  return false;
});
