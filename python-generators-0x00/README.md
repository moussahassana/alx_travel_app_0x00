# Python Generators Project

## Overview
This project implements a Python script to set up a MySQL database and handle data insertion from a CSV file for the ALX Backend Python curriculum.

## Repository Structure
- **Directory**: python-generators-0x00
- **Files**:
  - `seed.py`: Main script for database setup and data insertion
  - `.env`: Environment variables for MySQL credentials (not tracked in git)
  - `requirements.txt`: Python package dependencies
  - `README.md`: Project documentation

## Requirements
- Python 3.8+
- MySQL Server
- A CSV file named `user_data.csv` with columns: name, email, age

## Setup
1. Ensure MySQL server is running.
2. Install Python dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the project directory with MySQL credentials:
```plaintext
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
```
4. Place `user_data.csv` in the project directory.
5. Add `.env` to `.gitignore` to prevent committing sensitive data.

## Usage
Run the test script:
```bash
./main.py
```

This will:
1. Connect to MySQL using credentials from `.env`
2. Create ALX_prodev database
3. Create user_data table
4. Insert data from CSV
5. Display first 5 rows

## Database Schema
- **Database**: ALX_prodev
- **Table**: user_data
  - user_id: VARCHAR(36), Primary Key, Indexed
  - name: VARCHAR(255), NOT NULL
  - email: VARCHAR(255), NOT NULL
  - age: DECIMAL, NOT NULL