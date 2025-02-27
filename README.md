
# 🚀 **KeyLoggerProject**

A cutting-edge **key logging** and monitoring solution with a secure backend and modern API.

---

## 🌟 **Features**

- ✔️ **Real-time Keystroke Logging** – Capture and store keystrokes seamlessly.  
- ✔️ **End-to-End Encryption** – Secure sensitive data with robust encryption.  
- ✔️ **REST ful API with Flask** – Simple endpoints for data access and management.  
- ✔️ **Automated Error Reporting** – Instant logging of system errors.  
- ✔️ **Cross-Origin Support (CORS)** – Ensures smooth API integration.

---

## 📂 **Project Structure**

```
KeyLoggerProject/
├── agent/                  # Client-side keylogging agent
│   ├── main.py             # Main execution script
│   ├── key_logger_manager.py # Manages keylogging processes
│   ├── I_key_logger_service.py # Interface for keylogger services
│   ├── key_logger_service.py  # Implements keylogger services
│   ├── I_encryptor.py      # Interface for encryption
│   ├── xor_encryptor.py    # XOR-based encryption implementation
│   ├── I_writer.py         # Interface for writing methods
│   ├── file_writer.py      # Handles writing to files
│   ├── network_writer.py   # Handles network-based writing

├── back/                   # Backend API and data processing
│   ├── server.py           # Main backend server
│   ├── request_functions.py # Handles API requests
│   ├── users_data.py, users_data.json # Manages user-related data
│   ├── computers_names.py, computers_names.json # Manages computer names

├── front/                  # Frontend interface
│   ├── images/             # Contains UI images
│   │   ├── home_page.webp  # Homepage image
│   ├── login_page.html, login_page.js, login_page.css # Login page and its logic & styling
│   ├── home_page.html, home_page.js # Home page and its logic
│   ├── dates_page.html, dates_page.js # Page for selecting dates and its logic
│   ├── data_page.html, data_page.js # Data viewing page and its logic
│   ├── errors_page.html, errors_page.js # Errors log page and its logic
│   ├── style.css           # Global styling
│   ├── visual_template.drawio, visual_template.pdf # Visual app template

├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
```

---

## ⚡ **Quick Start**

### 📌 **Prerequisites**

Ensure you have the following installed:

- **Python 3.12**
- **Flask** (`Flask~=3.1.0`)
- **Flask-CORS** (`Flask-Cors~=5.0.0`)
- **dotenv** (`python-dotenv~=1.0.1`)
- **getmac** (`getmac~=0.9.5`)
- **requests** (`requests~=2.32.3`)
- **keyboard** (`keyboard~=0.13.5`)

### 🔧 **Installation**

Clone the repository and set up the environment:

```sh
$ git clone https://github.com/gavrielv/KeyLoggerProject.git
$ cd KeyLoggerProject
$ pip install -r requirements.txt
```

### 🌍 **Environment Setup**

#### **Agent**
Create a `.env` file in the `agent` directory and define the following variables:

```sh
URL=your_url_here  # Optional, default will be http://localhost:5000
ENCRYPTION_KEY=your_encryption_key  # Required
```

#### **Backend**
Create a `.env` file in the `back` directory and define the following variables:

```sh
BASE_DIR = your_base_directory_here  # Optional, default will be the current directory
DECRYPTION_KEY = your_decryption_key  # Required, must match the encryption key from the agent
```

### ▶️ **Running the Server**

```sh
$ python back/api/app.py
```

The Flask API will be available at `http://127.0.0.1:5000/`

---

### ▶️ **Running the Agent**

```sh
$ python agent/main.py
```

---

## 🌐 **API Endpoints**

### **🔵 POST Requests**

- `POST /api/upload` – Upload keystroke data.
- `POST /api/login` – Authenticate a user.
- `POST /api/send_error` – Send an error log.

### **🟢 GET Requests**

- `GET /api/get_machines_names` – Retrieve all monitored computers.
- `GET /api/get_dates_by_name/<name>` – Fetch available logs by computer.
- `GET /api/get_keystrokes_by_name_and_date/<name>/<date>` – Get keystroke logs.
- `GET /api/get_error_file` – Retrieve system error logs.

---

## 🔒 **Security Measures**

- 🔐 **Environment-Based Key Management** – Keeps credentials safe.  
- 🔐 **Data Encryption** – Prevents unauthorized access.  
- 🔐 **Structured API Authorization** – Ensures proper access control.  

---

## 🤝 **Contributing**

We welcome contributions! Feel free to open issues or submit pull requests.

---

## 📜 **License**

This project is licensed under the **MIT License**.

🚀 *Built with passion by the Gabriel team*
