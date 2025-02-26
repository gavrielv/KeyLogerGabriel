const url = 'http://127.0.0.1:5000';

// result[mac] = {'time': time, 'error_data': error_data}

const button = document.createElement("button");
button.textContent = "חזרה לדף הבית";
button.style.padding = "10px 20px";
button.style.fontSize = "16px";
button.style.cursor = "pointer";

document.body.appendChild(button);

// הוספת אירוע לחיצה
button.addEventListener("click", () => {
    window.location.href = "homePage.html";
});




// פונקציה להצגת הנתונים בדף    
const displayData = (data) => {
    // יצירת קונטיינר ראשי לכל הנתונים
    const container = document.createElement('div');
    container.classList.add("container");

    // יצירת כותרת
    const title = document.createElement('h1');
    title.innerText = `???????????????????????`;
    container.appendChild(title);

    // יצירת טבלה

    // יצירת ראש הטבלה
    const table = document.createElement('table');
    table.classList.add("data-table");
    const thead1 = document.createElement('thead');
    const tr1 = document.createElement('tr');

    const th1 = document.createElement('th');
    const th2 = document.createElement('th');
    const th3 = document.createElement('th');

    th1.innerText = "masin NAC";
    th2.innerText = "Time";
    th3.innerText = "error text";

    tr1.appendChild(th1);
    tr1.appendChild(th2);
    tr1.appendChild(th3);

    thead1.appendChild(tr1);
    table.appendChild(thead1);

    // יצירת גוף הטבלה (tbody)
    const tbody = document.createElement('tbody');

    // הוספת הנתונים לטבלה
    Object.keys(data).forEach(lineNum => {
        const tr = document.createElement('tr');
        const td1 = document.createElement('td');
        const td2 = document.createElement('td'); 

        td1.innerText = data[lineNum].mac;
        td2.innerText = data[lineNum].time;
        td3.innerText = data[lineNum].error

        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    container.appendChild(table);
    document.body.appendChild(container);

    }


async function fetchFollowingsData() {
    console.log("Fetching data..."); // הדפסת הודעה לקונסול
    console.log(`${url}/api/get_error_file`);
    try {
        const response = await fetch(`${url}/api/get_error_file`); // בקשה לשרת
        console.log(response);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        const followings = await response.json(); // המרת התגובה לאובייקט JSON
        console.log(followings);
        displayData(followings.machines); // יצירת כפתורים עם הנתונים שהתקבלו
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}






// fetchFollowingsData();