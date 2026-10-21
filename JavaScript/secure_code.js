// CodeAlpha Secure Coding Review
// Secure example: Safe DOM manipulation

function displayMessage(userInput) {
    const output = document.getElementById("output");

    // SECURE: Treat user input as plain text, not HTML.
    output.textContent = userInput;
}
