// Event listener for image upload input
document.getElementById("imageUpload").addEventListener("change", function(event) {
    const file = event.target.files[0]; // Get the selected file
    const preview = document.getElementById("imagePreview"); // Image preview element
    const alertBox = document.getElementById("alert-box"); // Alert box for messages
    const validFormats = ["image/jpeg", "image/jpg", "image/png"]; // Allowed file formats
    const maxSize = 2 * 1024 * 1024; // Maximum file size (2MB)

    // Reset alert box before validation
    alertBox.style.display = "none";
    alertBox.textContent = "";

    if (file) {
        // Validate file type
        if (!validFormats.includes(file.type)) {
            showAlert("Invalid file type! Only JPG, JPEG, and PNG are allowed.", "danger");
            event.target.value = ""; // Reset input field
            preview.style.display = "none"; // Hide preview
            return;
        }

        // Validate file size
        if (file.size > maxSize) {
            showAlert("File size exceeds 2MB. Please choose a smaller file.", "danger");
            event.target.value = ""; // Reset input field
            preview.style.display = "none"; // Hide preview
            return;
        }

        // Read file and display image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result; // Set preview image source
            preview.style.display = "block"; // Show preview
            showAlert("Image uploaded successfully!", "success");
        };
        reader.readAsDataURL(file); // Convert file to data URL
    }
});

/**
 * Displays an alert message on the page.
 * @param {string} message - The alert message to display.
 * @param {string} type - The type of alert (success, danger, etc.).
 */
function showAlert(message, type) {
    const alertBox = document.getElementById("alert-box");
    alertBox.className = `alert alert-${type}`; // Apply alert styling
    alertBox.textContent = message; // Set message content
    alertBox.style.display = "block"; // Show alert box

    // Automatically hide alert after 3 seconds
    setTimeout(() => { alertBox.style.display = "none"; }, 3000);
}

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const changePasswordCheckbox = document.getElementById("change-password-checkbox"); // Checkbox for changing password
    const passwordFields = document.getElementById("password-fields"); // Password input fields container
    const form = document.querySelector("form"); // The update form

    // Toggle password fields visibility when checkbox is checked/unchecked
    if (changePasswordCheckbox) {
        changePasswordCheckbox.addEventListener("change", function () {
            if (this.checked) {
                passwordFields.style.display = "block"; // Show password fields
            } else {
                passwordFields.style.display = "none"; // Hide password fields
            }
        });
    }

    // Add a hidden input field when submitting the form if password change is required
    form.addEventListener("submit", function () {
        if (changePasswordCheckbox.checked) {
            let hiddenInput = document.createElement("input");
            hiddenInput.type = "hidden";
            hiddenInput.name = "change_password";
            hiddenInput.value = "on"; // Mark that password change is requested
            form.appendChild(hiddenInput);
        }
    });
});
