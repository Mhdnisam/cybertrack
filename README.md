# Employment Management System

A comprehensive web-based application built with Django for managing employment-related activities. This system is designed to facilitate interaction between Project Managers, HRs, Employees, and Clients, streamlining tasks, attendance tracking, leave management, and communication.

## Features

This application supports multiple roles with dedicated dashboards and functionalities:

### 1. Roles & Authentication
- **Project Manager**: Dedicated login and dashboard to oversee project-related activities.
- **HR (Human Resources)**: Functionality to register, log in, and manage HR-specific tasks via a dashboard.
- **Employee (User)**: Registration and login for employees to view tasks, manage profile, and submit requests.
- **Client**: Client registration and login interface to track project progress or interact with the system.

### 2. Task Management
- **Create Tasks**: Administrators/Managers can create tasks with descriptions, deadlines, and assign them to employees.
- **View Tasks**: Employees can view their assigned tasks.
- **Update Status**: Employees can mark tasks as "Complete" or "Pending".

### 3. Attendance System
- **Mark Attendance**: Employees can mark their daily attendance (Present/Absent).
- **View Attendance**: Option to view attendance records for specific dates.
- **Attendance History**: Employees can track their attendance history.

### 4. Leave Management
- **Apply for Leave**: Employees can submit leave applications.
- **Leave Status**: Employees can check the status of their leave requests.
- **Manage Leave**: HR/Managers can approve or reject leave applications.

### 5. Requests & Feedback
- **Service Requests**: Users can submit generic requests and track their approval status.
- **Manage Requests**: Admin interface to approve or reject user requests.
- **Feedback System**: Users can submit feedback, which is viewable by administrators.

### 6. User Profile
- **View Profile**: Users can view their personal details.
- **Edit Profile**: Users can update their profile information.

## Technology Stack

- **Backend framework**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Database**: SQLite (Default) / PostgreSQL (Configurable)
- **Authentication**: Django Auth System

## Installation & Setup

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd employment
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (Optional, for Admin Panel access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    Open your browser and visit: `http://127.0.0.1:8000/`

## Usage

- **Project Manager**: Login with provided credentials (default code mentions `USER='employment'`, `PASS='12345'` - *Note: Update these in production!*).
- **HR**: Register a new HR account or login.
- **Employees**: Register a new user account to access the employee dashboard.
- **Clients**: Register as a client to access client-specific features.
