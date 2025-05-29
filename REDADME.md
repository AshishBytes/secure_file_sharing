# Secure File Sharing Backend 🚀

This is a secure file-sharing backend system built with FastAPI and MongoDB. It supports user roles, JWT-based authentication, secure file upload/download, and temporary download links.

---

## Features

- ✅ User registration and login (client & ops roles)
- 🔐 JWT authentication for protected routes
- 📁 Secure file upload by ops users
- 🔗 Temporary, expiring download links for clients
- 🧪 Optional: Test suite with `pytest`

---

## Installation

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

## Running the Server

```bash
uvicorn app.main:app --reload
```

Server will be available at:
📍 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## API Endpoints

### Auth Routes

* `POST /user/register` — Register user
* `POST /user/login` — Login and receive JWT token

### File Routes

* `POST /file/upload` — Upload a file (ops only)
* `GET /file/download-link/{filename}` — Generate download link (client)
* `GET /file/download/{token}` — Download file using token

🛡 Protected routes require:

```http
Authorization: Bearer <your-jwt-token>
```

---

## Project Structure

```
secure_file_sharing/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── utils/
├── requirements.txt
└── README.md
```

---

## Notes

* Use tools like **Postman** or **cURL** for testing the endpoints.
* You must create two users: one with `"role": "ops"` and one with `"role": "client"`.

---

## Author

Made with ❤️ by Ashish Singh – Backend Intern Challenge
