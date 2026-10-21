// CodeAlpha Secure Coding Review
// Example: Unsafe DOM manipulation
// Educational demonstration only.

// INSECURE: Never insert untrusted input using innerHTML.
function displayMessage(userInput) {
    const output = document.getElementById("output");
    output.innerHTML = userInput;
}