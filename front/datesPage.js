const url = 'http://127.0.0.1:5000'


// פונקציה לקריאת הפרמטר מה-URL
const getQueryParam = (param) => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
};


// פונקציה היוצרת את כפתורי המחשבים ומוסיפה אותם לדף
const createButtons = (dates) => {
    // יצירת קונטיינר ראשי לכל הכפתורים
    const container = document.createElement('div');
    container.classList.add("container");

    // יצירת כפתור לכל מחשב ברשימה
    dates.forEach(date => {
        const button = document.createElement('button');
        button.innerText = `data for \n ${date}`; // טקסט על הכפתור

        // בעת לחיצה על הכפתור, מעבר לדף עם פרמטר השם
        button.onclick = () => {
            window.location.href = `dataPage.html?name=${name1}&date=${encodeURIComponent(date)}`;
        };

        button.classList.add("my-button"); // הוספת מחלקה לכפתור
        container.appendChild(button); // הוספת הכפתור לקונטיינר
    });

    document.body.appendChild(container); // הוספת הקונטיינר לעמוד
};

// שליפת השם מה-URL
const name1 = getQueryParam("name");

async function fetchFollowingsData() {
    console.log("Fetching data..."); // הדפסת הודעה לקונסול
    console.log(`${url}/api/get_dates_by_name/${encodeURIComponent(name1)}`);
    try {
        const response = await fetch(`${url}/api/get_dates_by_name/${encodeURIComponent(name1)}`); // בקשה לשרת
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const followings = await response.json(); // המרת התגובה לאובייקט JSON
        createButtons(followings.dates); // יצירת כפתורים עם הנתונים שהתקבלו
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

if (name1) {
    console.log("Name is:", name1);
    fetchFollowingsData();
} else {    
    document.body.innerHTML = `<h1>No user selected</h1>`;
}