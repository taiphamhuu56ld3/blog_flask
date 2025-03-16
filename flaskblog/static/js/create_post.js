// Unsaved Changes Warning
let formChanged = false;

const titleInput = document.getElementById("post-title");
const contentInput = document.getElementById("post-content");
const postForm = document.getElementById("post-form");
const maxTitleLength = 100;

// Track changes to alert when leaving the page
titleInput.addEventListener("input", () => formChanged = true);
contentInput.addEventListener("input", () => formChanged = true);

// Title length limit
titleInput.addEventListener("input", function () {
    const remaining = maxTitleLength - this.value.length;
    let warningMessage = document.getElementById("title-length-warning");

    if (!warningMessage) {
        warningMessage = document.createElement("small");
        warningMessage.id = "title-length-warning";
        warningMessage.style.color = "red";
        this.parentNode.appendChild(warningMessage);
    }

    if (remaining < 0) {
        warningMessage.textContent = `Title is too long! Maximum ${maxTitleLength} characters allowed.`;
        this.classList.add("is-invalid");
    } else {
        warningMessage.textContent = `Remaining characters: ${remaining}`;
        this.classList.remove("is-invalid");
    }
});

// Warn user when leaving the page with unsaved changes
window.addEventListener("beforeunload", function (event) {
    if (formChanged) {
        event.preventDefault();
        event.returnValue = "You have unsaved changes. Are you sure you want to leave?";
    }
});

// Remove warning when form is submitted
postForm.addEventListener("submit", () => {
    formChanged = false;
});
