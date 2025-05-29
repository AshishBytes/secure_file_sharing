# Secure File Sharing Backend 🚀

This backend service enables secure file sharing with JWT authentication and role-based access control using FastAPI and MongoDB.

---

## 🔑 Features

- ✅ User registration and login (`client` & `ops` roles)
- 🔐 JWT authentication for protected routes
- 📁 Secure file uploads (only by `ops`)
- 📩 Temporary expiring download links (for `client`)
- ✉️ Email functionality: send the download link via email to client
- 🧪 Test suite with `pytest` (optional/bonus)

---

## ⚙️ Installation

```bash
git clone https://github.com/AshishBytes/secure-file-sharing.git
cd secure-file-sharing
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
````

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 User Authentication

### Register Users

**Client:**

```json
POST /user/register
{
  "email": "client@app.com",
  "password": "testpass",
  "role": "client"
}
```

**Ops:**

```json
POST /user/register
{
  "email": "ops@example.com",
  "password": "secureops",
  "role": "ops"
}
```

### Login

```json
POST /user/login
{
  "email": "client@app.com",
  "password": "testpass"
}
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>"
}
```

---

## 📁 File Upload (Ops only)

```http
POST /file/upload
Headers:
Authorization: Bearer <ops-token>
Content-Type: multipart/form-data
```

---

## 🔗 Generate Download Link (Client)

```http
GET /file/download-link/<filename>
Headers:
Authorization: Bearer <client-token>
```

Response:

```json
{
  "download_url": "http://127.0.0.1:8000/file/download/<token>"
}
```

---

## ⬇️ File Download (Using Token)

```http
GET /file/download/<token>
```

---

## ✉️ Email Feature (Bonus)

Add the following to your `.env`:

```env
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_app_password
MAIL_FROM=your_email@example.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME="SecureShare"
```

Then call:

```http
POST /file/send-email/<filename>
Headers:
Authorization: Bearer <client-token>
Body:
{
  "to_email": "client@app.com"
}
```

This sends the generated link to the email securely.

---

## 📂 Project Structure

```
secure_file_sharing/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── utils/
├── tests/
├── .env
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests (Optional Bonus)

You can run all test cases using:

```bash
$env:PYTHONPATH = "."        # Windows
export PYTHONPATH=.          # macOS/Linux

pytest tests/
```

> Make sure `report.docx` is in your project root or adjust the test file accordingly.

---

## 👨‍💻 Author

Made with ❤️ by **Ashish Singh** — For Backend Intern Test.
