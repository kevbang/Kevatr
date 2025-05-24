# About Kevatr

<img width="743" alt="image" src="https://github.com/user-attachments/assets/8c9d39fc-9194-4973-83e2-462cef9f57bb" />

# 🚀 Project Overview

## 🧩 Summary

This full-stack web application allows users to log in using either a **custom login system** or **OAuth (GitHub or Spotify)**. It uses:

- **React + TypeScript** for the frontend interface
- **Flask (Python)** for the backend API and business logic
- **Amazon RDS (PostgreSQL)** for storing user and application data
- **Docker** for containerized deployment of both frontend and backend services

External APIs like **GitHub** and **Spotify** are integrated to fetch and store user data.

---

## 🧱 Architecture Components

### 🖥️ Frontend

- **Tech:** React + TypeScript
- **Role:**
  - Handles user interface and routing
  - Sends API requests to the Flask backend
  - Supports both custom and OAuth login flows
- **Communication:**
  - REST API calls to backend
  - Sends login credentials (custom or OAuth)

---

### 🧠 Backend

- **Tech:** Flask (Python)
- **Role:**
  - Handles API requests from the frontend
  - Manages user authentication and sessions
  - Communicates with the database and external APIs
- **Authentication:**
  - **Custom Auth**: traditional username/password logic
  - **OAuth**: GitHub and Spotify login support

---

### 🗃️ Database

- **Tech:** Amazon RDS (PostgreSQL)
- **Role:**
  - Stores user data, tokens, and app-related information
  - Handles secure queries from the Flask backend

---

### 🌍 External APIs

- **GitHub API**:
  - Used to retrieve user repositories or GitHub profile info
- **Spotify API**:
  - Used to fetch playlists or current track information

---

### 🐳 Docker Deployment

- **Components:**
  - Frontend Container (React app)
  - Backend Container (Flask API)
- **Benefits:**
  - Easy deployment and scalability
  - Consistent development and production environments

---

## 🔄 How It Works

1. User accesses the React frontend.
2. User logs in via:
   - **Custom login**: credentials sent to Flask backend
   - **OAuth login**: redirected to GitHub/Spotify for authorization
3. Flask backend handles the login logic and generates a session/token.
4. Frontend makes **REST API calls** to fetch user data.
5. Backend:
   - Talks to **Amazon RDS** to read/write user info
   - Uses **external APIs** to fetch live GitHub/Spotify data
6. All components are deployed using Docker containers.

---

## ✅ Key Features

- 🔐 Dual login system (Custom + OAuth)
- ☁️ Secure cloud database (Amazon RDS)
- ⚙️ Backend logic and API in Python
- 💻 Frontend in React/TypeScript
- 🐳 Dockerized deployment for easy setup and scaling
- 🌐 Integration with GitHub and Spotify for real-time data access



