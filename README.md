
# 🔐 Caesar Cipher Web App

A simple and secure **Caesar Cipher encryption/decryption web application** built using **Flask**. This project was developed as part of a **Cybersecurity Internship** to demonstrate understanding of classical encryption methods, secure coding practices, and web application development.

---

## 🚀 Features

- Encrypt and Decrypt text using the Caesar Cipher algorithm
- Clean, responsive web interface
- Input validation for secure handling
- Preserves spaces, punctuation, and case
- Easy to host locally or on platforms like Render, Hostinger, or Replit

---

## 🧠 What is Caesar Cipher?

The Caesar Cipher is a substitution cipher that shifts characters in the alphabet by a fixed number of positions. It’s one of the oldest encryption techniques used by Julius Caesar to securely communicate.

> Example:  
> `A` with shift `+3` becomes `D`  
> `HELLO` → `KHOOR`

---

## 🖥️ Technologies Used

- Python 3
- Flask
- HTML5 / CSS3 (with basic styling)

---

## 📁 Project Structure

```
caesar_cipher_web/
├── app.py                  # Main Flask app
├── templates/
│   └── index.html          # Web interface (form + output)
└── static/
    └── style.css           # CSS styling
```

---

## 📦 Installation & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/letchagan/SCT_CS_1
cd caesar-cipher-web
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Flask
```bash
pip install flask
```

### 4. Run the app
```bash
python app.py
```

Then open your browser and go to:  
👉 `http://127.0.0.1:5000`

---

## 🧪 Sample Input

- **Text**: `CyberSecurityIntern`  
- **Shift**: `3`  
- **Mode**: `Encrypt`  
- **Result**: `FbehuVhfxulwbLqwhuq`

---

## 🌐 Hosting

You can deploy this app using:
- [Render](https://render.com/)
- [Replit](https://replit.com/)
- Hostinger (via Flask + WSGI support)
- [GitHub Pages + Flask Hosting](https://docs.github.com/en/pages) (with backend services like Railway or PythonAnywhere)

---

## 🔒 Future Improvements

- Brute-force decryption mode
- File encryption & decryption
- User authentication (Flask-Login)
- Export result to `.txt`
- Add security headers and CSRF protection

---

## 👨‍💻 Developed By

**Letchagan A**  
Cybersecurity Intern  
India  
[GitHub](https://github.com/yourusername)

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🤝 Acknowledgment

Built with ❤️ by **Letchagan A** for a **Cybersecurity Internship Project**, showcasing classical encryption, secure input handling, and web app development.
