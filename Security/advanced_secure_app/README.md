# Advanced Secure App

## Overview

This project is an advanced secure crypting application built with Flask. It includes features such as user and admin authentication, secure password storage, and logging. The application ensures data security through encryption and decryption functionalities, making it suitable for handling sensitive information.

## Project Structure

```plaintext
advanced_secure_app/
├── .gitignore
├── add_admin.py
├── app/
│   ├── init.py
│   ├── config.py
│   ├── extensions.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── admin_login.html
│   │   ├── dashboard.html
│   │   ├── admin_dashboard.html
│   ├── static/
│   │   └── styles.css
├── config.py
├── create_database.py
├── delete_admin.py
├── logs/
│   └── app.log
├── README.md
├── requirements.txt
├── run.py
```

## Features

- **User Authentication**: Secure login and registration system.
- **Admin Authentication**: Separate admin login with additional privileges.
- **Secure Password Storage**: Passwords are hashed using industry-standard algorithms.
- **Logging**: Comprehensive logging for monitoring and debugging.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/advanced_secure_app.git
    ```

2. Navigate to the project directory:

    ```sh
    cd advanced_secure_app
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```sh
    python run.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.
