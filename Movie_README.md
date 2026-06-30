# Movie Explorer & Review Management System

A full-stack web application designed to view, search, and manage a curated list of movies. Built using **FastAPI** for a fast, light backend API and **Streamlit** for a clean, user-friendly frontend interface.

---

## 🚀 Key Features

### Frontend UI (Streamlit)
* **Sidebar Navigation:** Effortlessly toggle between application pages via a dropdown menu.
* **View All Movies:** Dynamically load and inspect all movies within the database.
* **Filter Options:** Search films dynamically by **Genre**, **Language**, or **Minimum Rating** using interactive slider and dropdown widgets.
* **Full Form Actions:** Standard input fields to create new entries, alter movie attributes, or drop items directly from the backend.

### Backend API (FastAPI)
* **Full CRUD Operations:** Custom endpoints managing resources via standard `GET`, `POST`, `PUT`, and `DELETE` requests.
* **Dynamic Parameter Validation:** Utilizes path parameters to target specific IDs and query parameters to filter responses cleanly.
* **In-Memory Store:** Optimized architecture running a lightweight in-memory storage array for rapid data alterations.
* **Built-in Docs:** Fully supported interactive interactive API testing suite available locally via Swagger UI.

---

## 🛠️ Technologies Used

* **Frontend:** [Streamlit](https://streamlit.io) (UI & User Interaction)
* **Backend:** [FastAPI](https://tiangolo.com) (API Design & Business Logic)
* **Server:** [Uvicorn](https://uvicorn.org) (FastAPI ASGI Server)
* **Communication:** [Requests](https://readthedocs.io) (HTTP Client Library)

---

## 📂 Project Structure

Organize your local development setup to mirror the architectural design layout below:

```text
movie_project/
│
├── backend/
│   └── main1.py         # FastAPI Application & Endpoints
│
├── frontend/
│   └── app1.py          # Streamlit Web App Interface
│
└── requirements.txt     # Python Dependencies
```

---

## ⚙️ Installation & Setup Instructions

Follow these step-by-step terminal instructions to configure and run the application locally:

### Step 1: Install Dependencies
Open your terminal environment and install the required library ecosystem:
```bash
pip install fastapi uvicorn streamlit requests
```

### Step 2: Fire Up the Backend Server
Navigate into your backend source folder directory and boot up the server engine:
```bash
cd backend
uvicorn main:app --reload
```
*The API baseline will initialize locally. You can explore or test backend routing structures via the interactive [Swagger Documentation Hub](http://127.0.0).*

### Step 3: Launch the Frontend Web Client
Open a fresh parallel terminal window, navigate into your frontend UI source layout, and start the script:
```bash
cd frontend
streamlit run app.py
```

---

## 🔄 Core Application Workflow

This project maps a real-world foundational software lifecycle layout through a clear, systematic data route:

```text
User Actions (UI) ➡️ Streamlit Frontend ➡️ 'Requests' Module (HTTP methods) ➡️ FastAPI Backend ➡️ CRUD Execution on Memory Data ➡️ JSON Return Payload ➡️ Dynamic Interface Repaint
```

