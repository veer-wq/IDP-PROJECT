console.log("Composite Materials Engineering Platform loaded.");


// Update footer year automatically
const yearElement = document.getElementById("currentYear");

if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
}