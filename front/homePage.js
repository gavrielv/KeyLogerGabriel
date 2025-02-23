const claints = ['avi','ben','david','daniel','eli','guy','gadi','haim','idan','jacob','liran','moran','nir','omer','ron','shay','tal','uri','yosi','ziv'];

const f = (claints) => {
    console.log('Hello World');
    const div1 = document.createElement('div');
    div1.classList.add("container");
    claints.forEach ( (claint) => {
        const button = document.createElement('button');
        button.innerText = `for ${claint} cleck me`;
        // מעבר לדף profile.html עם פרמטר של השם
        button.onclick = () => {
            window.location.href = `http://127.0.0.1:5000/user?name=${encodeURIComponent(claint)}`;
        };
        button.classList.add("my-button");
        div1.appendChild(button)
    })
    document.body.appendChild(div1);
}


async function fetchfollowingsData() {
    console.log("Fetching data..."); // הדפסת הודעה לקונסול
    try {
        const response = await fetch("http://127.0.0.1:5000/items"); // קריאה לשרת
        console.log("Response:", response); // הצגת התגובה בקונסול
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`); // בדיקת שגיאות
        }
        const followings = await response.json(); // המרת התגובה לאובייקט JSON
        console.log("Data:",followings ); // הצגת הנתונים בקונסול
        f(followings); // קריאה לפונקציה שתציג את הנתונים בדף
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
console.log("dfsdgfgdfsdasdadfgdh")
fetchfollowingsData();