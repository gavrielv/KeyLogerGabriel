// רשימת הלקוחות
// const clients = ['avi','ben','david','daniel','eli','guy','gadi','haim','idan','jacob','liran','moran','nir','omer','ron','shay','tal','uri','yosi','ziv'];


const url = 'http://127.0.0.1:5000'


// פונקציה היוצרת את הכפתורים ומוסיפה אותם לדף
const createButtons = (computers) => {
    // יצירת קונטיינר ראשי לכל הכפתורים
    const container = document.createElement('div');
    container.classList.add("container");

    // יצירת כפתור לדף השגיאות
    const errorButton = document.createElement('button');
    errorButton.innerText = "Errors Page"; // טקסט על הכפתור
    errorButton.onclick = () => {
        window.location.href = "erorrsPage.html"; // מעבר לדף השגיאות
    };
    errorButton.classList.add("my-button"); // הוספת מחלקה לכפתור
    container.appendChild(errorButton); // הוספת הכפתור לקונטיינר

    // יצירת כפתור לכל מחשב ברשימה
    computers.forEach(computer => {
        const button = document.createElement('button');
        button.innerText = `For ${computer} \n click me`; // טקסט על הכפתור

        // בעת לחיצה על הכפתור, מעבר לדף עם פרמטר השם
        button.onclick = () => {
            window.location.href = `datesPage.html?name=${encodeURIComponent(computer)}`;
        };

        button.classList.add("my-button"); // הוספת מחלקה לכפתור
        container.appendChild(button); // הוספת הכפתור לקונטיינר
    });

    document.body.appendChild(container); // הוספת הקונטיינר לעמוד
};

// פונקציה היוצרת את הכותרת וההסבר בראש הדף
const createHeader = () => {
    const header = document.createElement('div');
    header.classList.add("header");

    const title = document.createElement('h1');
    title.innerText = "Welcome to the Client Portal"; // כותרת ראשית

    const description = document.createElement('p');
    description.innerText = "Click on a client's button to view their profile."; // הסבר קצר

    header.appendChild(title);
    header.appendChild(description);
    document.body.appendChild(header); // הוספת הכותרת לדף
};

// פונקציה לקבלת נתונים מהשרת
async function fetchFollowingsData() {
    console.log("Fetching data..."); // הדפסת הודעה לקונסול
    console.log(`${url}/api/get_machines_names`);
    try {
        const response = await fetch(`${url}/api/get_machines_names`); // בקשה לשרת
        console.log(response);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const followings = await response.json(); // המרת התגובה לאובייקט JSON
        console.log(followings);
        createButtons(followings.machines); // יצירת כפתורים עם הנתונים שהתקבלו
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// יצירת כותרת והסבר לפני טעינת הכפתורים
createHeader();
fetchFollowingsData(); // קריאה לפונקציה שמביאה את הנתונים מהשרת
