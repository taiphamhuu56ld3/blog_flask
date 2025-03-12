// Disable right click
document.addEventListener('contextmenu', (e) => e.preventDefault());

// Disable F12, Ctrl + Shift + I, Ctrl + Shift + J, Ctrl + U
function ctrlShiftKey(e, keyCode) {
  return e.ctrlKey && e.shiftKey && e.keyCode === keyCode.charCodeAt(0);
}

document.onkeydown = (e) => {
  if (
    event.keyCode === 123 ||
    ctrlShiftKey(e, 'I') ||
    ctrlShiftKey(e, 'J') ||
    ctrlShiftKey(e, 'C') ||
    (e.ctrlKey && e.keyCode === 'U'.charCodeAt(0))
  )
    return false;
};

// Toggle icon on navbar
var icon = document.getElementById("icon");

icon.onclick = function () {
    document.body.classList.toggle("bright-theme");
    var iconElement = icon.querySelector('i');

    if (document.body.classList.contains("bright-theme")) {
        iconElement.classList.replace('bx-sun', 'bx-moon');
        localStorage.setItem("theme", "bright");
    } else {
        iconElement.classList.replace('bx-moon', 'bx-sun');
        localStorage.setItem("theme", "dark");
    }
};

// Load theme from localStorage when reopen page
if (localStorage.getItem("theme") === "bright") {
    document.body.classList.add("bright-theme");
    icon.querySelector('i').classList.replace('bx-sun', 'bx-moon');
}
