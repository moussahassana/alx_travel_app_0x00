
# ALX Travel App

This project contains multiple Python modules for managing a travel and messaging application, including testing, asynchronous context management, decorators, and generators.

## Project Structure

- `messaging_app/`  
  A Django application for messaging and listings management. It includes two main apps:  
  - `chats/`: handles conversations  
  - `listings/`: manages listings and includes data seeding commands  
  The project uses a SQLite database `db.sqlite3` and the Django management script `manage.py`.

- `0x03-Unittests_and_integration_tests/`  
  Unit and integration tests for various Python modules, including client, utils, and fixtures.

- `python-context-async-perations-0x02/`  
  Scripts demonstrating context management, database connections, and asynchronous operations.

- `python-decorators-0x01/`  
  Examples of Python decorators for logging, transactional control, retry logic, caching, and more.

- `python-generators-0x00/`  
  Scripts showing usage of Python generators for batch processing, lazy pagination, streaming, etc.

  
```
alx_travel_app_0x00
├─ 0x03-Unittests_and_integration_tests
│  ├─ client.py
│  ├─ fixtures.py
│  ├─ README.md
│  ├─ test_client.py
│  ├─ test_utils.py
│  ├─ utils.py
│  └─ __init__.py
├─ LICENSE
├─ messaging_app
│  ├─ chats
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ db.sqlite3
│  ├─ listings
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ management
│  │  │  └─ commands
│  │  │     ├─ seed.py
│  │  │     └─ __init__.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ manage.py
│  └─ messaging_app
│     ├─ asgi.py
│     ├─ settings.py
│     ├─ urls.py
│     ├─ wsgi.py
│     └─ __init__.py
├─ poetry.lock
├─ pyproject.toml
├─ python-context-async-perations-0x02
│  ├─ 0-databaseconnection.py
│  ├─ 1-execute.py
│  └─ 3-concurrent.py
├─ python-decorators-0x01
│  ├─ 0-log_queries.py
│  ├─ 1-with_db_connection.py
│  ├─ 2-transactional.py
│  ├─ 3-retry_on_failure.py
│  └─ 4-cache_query.py
├─ python-generators-0x00
│  ├─ 0-stream_users.py
│  ├─ 1-batch_processing.py
│  ├─ 1-main.py
│  ├─ 2-lazy_paginate.py
│  ├─ 3-main.py
│  ├─ 4-stream_ages.py
│  ├─ main.py
│  ├─ README.md
│  └─ seed.py
├─ README.md
├─ requirements.txt
├─ users.db
└─ user_data.csv

```

## Key Files

- `requirements.txt`: Python dependencies  
- `pyproject.toml` & `poetry.lock`: Poetry configuration and lock files  
- `users.db` and `user_data.csv`: User data for testing and demonstration purposes

## Installation

```bash
poetry install

