// loginPage.js

document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // מונע טעינה מחדש של הדף

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    //  למלאאןת כתובת השרת
    const serverUrl = "[YOUR_SERVER_URL]";

    try {
        const response = await fetch(serverUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            window.location.href = "homePage.html"; // שולח לדף הבית
        } else {
            document.getElementById("errorMessage").innerText = "Invalid credentials. Please try again.";
        }
    } catch (error) {
        console.error("Login failed:", error);
        document.getElementById("errorMessage").innerText = "Server error. Please try again later.";
    }
});
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("seePassword").addEventListener("click", function() {
        const passwordField = document.getElementById("password");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            this.innerText = "Hide";
        } else {
            passwordField.type = "password";
            this.innerText = "Show";
        }
    });
});
