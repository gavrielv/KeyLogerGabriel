// פונקציה לקריאת הפרמטר מה-URL
const getQueryParam = (param) => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
};

// שליפת השם מה-URL
const name1 = getQueryParam("name");

console.log("Query param name:", name1); // בדיקה אם הפרמטר נשלף

if (name1) {
    console.log(`Fetching data for: ${name1}`);

    // שליחת בקשה לשרת
    fetch(`http://127.0.0.1:5000/user?name=${encodeURIComponent(name1)}`)
        .then(response => {
            console.log("Response status:", response.status); // בדיקת סטטוס התגובה
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("User data:", data); // בדיקת הנתונים שהתקבלו
            if (data.error) {
                document.body.innerHTML = `<h1>User Not Found</h1>`;
            } else {
                document.body.innerHTML = `
                    <h1>Welcome, ${data.name}</h1>
                    <p>Age: ${data.age}</p>
                    <p>City: ${data.city}</p>
                `;
            }
        })
        .catch(error => {
            console.error("Error fetching user data:", error);
            document.body.innerHTML = `<h1>Error loading user data: ${error.message}</h1>`;
        });
} else {
    document.body.innerHTML = `<h1>No user selected</h1>`;
}