# 🔐 Secure File Sharing Backend

This is a secure file-sharing backend system built with **FastAPI** and **MongoDB**. It supports user roles, JWT-based authentication, secure file upload/download, email verification, and time-limited download links.

---

## 🚀 Features

- ✅ User registration (`client` role only)
- ✅ JWT-based login for secure access
- ✅ Role-based access control (`client` & `ops`)
- ✅ Email verification required for clients
- ✅ Secure file upload by `ops` users
- ✅ Generate temporary download links for files
- ✅ Access file via secure token before expiry

---

## 🛠 Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB (via Motor)
- **Auth:** JWT (PyJWT)
- **Mail:** SMTP (Gmail / Mailtrap)
- **Hashing:** Passlib (bcrypt)

---

## 📁 Project Structure

```

secure\_file\_sharing/
├── app/
│   ├── main.py                # FastAPI app
│   ├── core/                  # MongoDB config
│   ├── models/                # Pydantic models
│   ├── routes/                # User & file routes
│   └── utils/                 # JWT, hashing, email
├── .env                       # Environment variables
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

```bash
git clone https://github.com/AshishBytes/secure-file-sharing.git
cd secure-file-sharing
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux

pip install -r requirements.txt
````

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at:
📍 `http://127.0.0.1:8000`

---

## 🔐 Authentication

JWT token is returned on login and required for protected routes.

**Headers:**

```
Authorization: Bearer <access_token>
```

---

## 🔧 Environment Variables (`.env`)

```
MONGO_URI=mongodb://localhost:27017
JWT_SECRET=your_secret_key
JWT_EXPIRE_MINUTES=15
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_password_or_app_password
```

> 📌 Use [Mailtrap](https://mailtrap.io/) or Gmail App Password for email testing.

---

## 🧪 Sample Users

Use these to test in Postman or Swagger UI:

### ✅ OPS User

```json
{
  "email": "ops@example.com",
  "password": "secureops"
}
```

### ✅ CLIENT User

```json
{
  "email": "client@app.com",
  "password": "testpass"
}
```

---

## 🧾 API Endpoints

### 👤 User Routes

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| POST   | `/user/signup`      | Register a new client   |
| GET    | `/user/verify/{id}` | Verify client email     |
| POST   | `/user/login`       | Login for client or ops |

---

### 📁 File Routes

| Method | Endpoint                         | Description                     |
| ------ | -------------------------------- | ------------------------------- |
| POST   | `/file/upload`                   | Upload file (ops only)          |
| GET    | `/file/download-link/{filename}` | Generate download link (client) |
| GET    | `/file/download/{token}`         | Download file with token        |

---


## 🧑‍💻 Author

Made with ❤️ by **Ashish Singh**

---

## 📌 TODO (Optional Enhancements)

* [ ] Add automated email testing via Mailtrap
* [ ] Add frontend integration (e.g., React)
* [ ] Add rate limiting or audit logging
* [ ] Finalize unit tests for full coverage