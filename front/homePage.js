

const url = 'http://127.0.0.1:5000'

    const DevicesList = document.createElement('div');
    DevicesList.classList.add("DevicesList");
    const device = document.createElement('h2');
    device.innerText = "Devices";
    DevicesList.appendChild(device);

// פונקציה היוצרת את הכפתורים ומוסיפה אותם לדף
const createButtons = (computers) => {
    // יצירת קונטיינר ראשי לכל הכפתורים
    const container = document.createElement('div');
    container.classList.add("container");





    // יצירת כפתור לכל מחשב ברשימה
    computers.forEach(computer => {
        const button = document.createElement('button');
        button.innerText = `${computer}`; // טקסט על הכפתור

        // בעת לחיצה על הכפתור, מעבר לדף עם פרמטר השם
        button.onclick = () => {
            window.location.href = `datesPage.html?name=${encodeURIComponent(computer)}`;
        };

        button.classList.add("my-button"); // הוספת מחלקה לכפתור
        container.appendChild(button); // הוספת הכפתור לקונטיינר
    });

    // יצירת כפתור לדף השגיאות
    const errorButton = document.createElement('button');
    errorButton.classList.add("errorButton");
    errorButton.innerText = "Errors Page"; // טקסט על הכפתור
    errorButton.onclick = () => {
        window.location.href = "erorrsPage.html"; // מעבר לדף השגיאות
    };
    errorButton.classList.add("my-button"); // הוספת מחלקה לכפתור
    container.appendChild(errorButton); // הוספת הכפתור לקונטיינר

    document.body.appendChild(DevicesList); // הוספת DevicesList קודם
    document.body.appendChild(container);   // הוספת הקונטיינר אחריו

};

// פונקציה היוצרת את הכותרת וההסבר בראש הדף
const createHeader = () => {
    const header = document.createElement('div');
    header.classList.add("header");

    const title = document.createElement('h1');
    title.innerText = "Welcome Soldier"; // כותרת ראשית
    header.appendChild(title);
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
