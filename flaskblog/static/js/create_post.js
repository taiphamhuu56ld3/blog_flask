// Unsaved Changes Warning
let formChanged = false;
    
document.getElementById("post-title").addEventListener("input", () => formChanged = true);
document.getElementById("post-content").addEventListener("input", () => formChanged = true);

window.addEventListener("beforeunload", function (event) {
    if (formChanged) {
        event.preventDefault();
        event.returnValue = "You have unsaved changes. Are you sure you want to leave?";
    }
});

document.getElementById("post-form").addEventListener("submit", () => {
    formChanged = false; // Reset formChanged when form is submitted
});
