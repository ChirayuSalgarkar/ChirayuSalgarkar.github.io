// password-protect.js
function passwordProtect() {
    var password = prompt("Enter the password to access this page:");
    if (password !== 'qpvaj8') { 
        alert('Incorrect password. Access denied.');
        window.location.href = '/'; 
}
