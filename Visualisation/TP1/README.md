# TP1 - Visualisation

## Overview

This project demonstrates the use of SQLAlchemy for database management in a Python application. SQLAlchemy is a powerful and flexible Object-Relational Mapping (ORM) library that allows developers to interact with databases using Python code. In this project, we create a SQLite database with a `users` table and perform basic CRUD (Create, Read, Update, Delete) operations.

## SQLAlchemy

### What is SQLAlchemy?

SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access. SQLAlchemy's ORM allows developers to map Python classes to database tables, making it easier to interact with the database using Python code.

### Key Features of SQLAlchemy

- **ORM (Object-Relational Mapping)**: Map Python classes to database tables and vice versa.
- **SQL Expression Language**: Write SQL queries using Python expressions.
- **Schema Definition**: Define database schemas using Python classes.
- **Session Management**: Manage database transactions and sessions.
- **Database Agnostic**: Supports multiple database backends, including SQLite, PostgreSQL, MySQL, and more.

## Project Structure

```
Visualisation/
├── models.py       # Defines the database models and schema
├── create_db.py    # Script to create the database and tables
├── add_user.py     # Script to add a new user to the database
├── README.md       # Project documentation
└── app.db          # SQLite database file (created after running create_db.py)
```