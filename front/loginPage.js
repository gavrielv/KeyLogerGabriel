const url = 'http://127.0.0.1:5000';

// פונקציה שמבצעת התחברות
const handleLogin = (event) => {
    event.preventDefault(); // מונע מהטופס לרענן את הדף

    // קבלת פרטי המשתמש מהטופס
    const user_name = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("error-message");

    // בדיקה אם השדות ריקים
    if (!user_name || !password) {
        errorMessage.innerText = "Username and password cannot be empty!";
        errorMessage.style.color = "red";
        return;
    }

    // יצירת אובייקט עם פרטי המשתמש
    const data = {
        user_name: user_name,
        password: password
    };
    console.log(data);
    // שליחת הפרטים לשרת
    fetch(`${url}/api/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "homePage.html";
        } else {
            errorMessage.innerText = "Invalid username or password!";
            errorMessage.style.color = "red";
        }
    })
    .catch(error => {
        console.error("Error logging in:", error);
        errorMessage.innerText = "Server error, please try again later.";
        errorMessage.style.color = "red";
    });
};
const togglePasswordVisibility = () => {
    event.preventDefault()

    const passwordInput = document.getElementById("password");
    const togglePassword = document.getElementById("seePassword");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.innerHTML = "🙈"; // משנה אייקון
    } else {
        passwordInput.type = "password";
        togglePassword.innerHTML = "👁️";
    }
};


// פונקציה ליצירת חלון ההתחברות
const loginWindow = () => {
    // יצירת אלמנט הקונטיינר
    const login = document.createElement('div');
    login.classList.add("login-container");

    // יצירת כותרת
    const title = document.createElement('h1');
    title.innerText = "Login";
    login.appendChild(title);

    // יצירת טופס
    const form = document.createElement('form');
    form.classList.add("login-form");

    // יצירת שדה שם משתמש
    const input1 = document.createElement('input');
    input1.type = "text";
    input1.placeholder = "Username";
    input1.id = "username";

    // יצירת קונטיינר לסיסמה
    const passwordContainer = document.createElement('div');
    passwordContainer.classList.add("password-container");

    // יצירת שדה סיסמה
    const input2 = document.createElement('input');
    input2.type = "password";
    input2.placeholder = "Password";
    input2.id = "password";
    input2.classList.add("password-container");

    // יצירת כפתור הצגת סיסמה
    const togglePassword = document.createElement('button');
    togglePassword.id = "seePassword";
    togglePassword.innerHTML = "👁️";
    togglePassword.type = "button"; // מונע שליחה בטעות
    togglePassword.addEventListener("click", togglePasswordVisibility); // קריאה לפונקציה

    // הוספת אלמנטים לקונטיינר של הסיסמה
    passwordContainer.appendChild(input2);
    passwordContainer.appendChild(togglePassword);


    // יצירת כפתור התחברות
    const submit = document.createElement('button');
    submit.innerText = "Login";
    submit.type = "submit"; // חשוב שהכפתור יהיה בתוך הטופס

    // יצירת הודעת שגיאה
    const errorMessage = document.createElement('p');
    errorMessage.id = "error-message";
    errorMessage.style.color = "red";

    // הוספת אלמנטים לטופס ולדף
    form.appendChild(input1);
    form.appendChild(passwordContainer);
    form.appendChild(submit);
    form.appendChild(errorMessage);
    login.appendChild(form);
    document.body.appendChild(login);

    // הוספת מאזין אירוע לטופס כדי למנוע רענון דף
    form.addEventListener("submit", handleLogin);
};

// יצירת חלון הלוגין
loginWindow();
