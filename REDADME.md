# 🚀 Secure File Sharing Backend

This is a secure file-sharing backend system built with **FastAPI** and **MongoDB**. It supports user roles, JWT-based authentication, email verification, encrypted file handling, and temporary download links.

---

## ✨ Features

- ✅ User registration & login with roles (`client`, `ops`)
- ✉️ Email-based verification before file access
- 🔐 JWT authentication for secure endpoints
- 📁 File upload support (ops only)
- 🔗 Expiring encrypted download links (for clients)
- ❌ Test suite not implemented yet (future scope)

---

## 🛠 Tech Stack

- **FastAPI** – Web framework
- **MongoDB** – NoSQL database
- **PyJWT** – JWT-based auth
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server
- **passlib** – Password hashing

---

## 📁 Project Structure

```

secure\_file\_sharing/
├── app/
│   ├── main.py              # FastAPI app setup
│   ├── models/              # Pydantic & MongoDB models
│   ├── routes/              # API route handlers
│   └── utils/               # JWT, auth, helpers
├── tests/                   # (Future) test cases
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

````

---

## 🚀 Installation

```bash
git clone https://github.com/AshishBytes/secure-file-sharing.git
cd secure-file-sharing

python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
````

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 API Endpoints

### ✅ Auth Routes

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/user/register` | Register new user |
| POST   | `/user/login`    | Login and get JWT |

**🔧 Example JSON for Signup/Login**:

```json
// OPS User Registration/Login
{
  "email": "ops@example.com",
  "password": "secureops",
  "role": "ops"
}

// Client User Registration/Login
{
  "email": "client@app.com",
  "password": "testpass",
  "role": "client"
}
```

---

### 📁 File Routes

| Method | Endpoint                         | Description                     |
| ------ | -------------------------------- | ------------------------------- |
| POST   | `/file/upload`                   | Upload file (ops only)          |
| GET    | `/file/download-link/{filename}` | Generate expiring download link |
| GET    | `/file/download/{token}`         | Download file using valid token |

> 🔒 All protected routes require this header:
>
> ```
> Authorization: Bearer <your-jwt-token>
> ```

---

## 📦 Testing With Postman

1. **Register Users** at `/user/register` with above JSON.
2. **Login** via `/user/login` to receive a JWT.
3. Use `Authorization: Bearer <token>` for protected routes.

---

## 📌 Notes

* Create at least two users:

  * One with `"role": "ops"` to upload files
  * One with `"role": "client"` to download files
* Use **Postman**, **Thunder Client**, or **cURL** for testing.
* Encrypted JWT tokens include:

  * `filename`
  * `user email`
  * `expiration time`

---

## ⚠️ Missing

* ❌ Automated test cases (pytest)
* ❌ Frontend integration
* ❌ Admin dashboard

---

## 👤 Author

Built with ❤️ by **Ashish Singh**
