# Triple -A- Expenses

A simple web app useful for managing both expenses and income.

## Features

- Feature 1: creating a user account using an email account.
- Feature 2: add,modify or delete an income or expense.
- Feature 3: visualize your date in a chart.
- Feature 4:Have a comparison btween income and expenses.

## Prerequisites

To run this project, you’ll need to have the following installed:
- Python (3.12.0)
- Django (5.1)
- PostgreSQL 16 =>pgAdmin 4 
- Postman
- pip (22.2.2)
- pip install -r requirements.txt
- pip install psycopg2-binary
- pip install django-crispy-forms
- pip install django-chartjs
- pip install django-filter



## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/aymenayoun/Triple-A

### Step 2: Navigate to the project directory

```bash
cd expenseswebsite

### Step 3: Set up a virtual environment

```bash
python -m venv venv
## Activate the virtual environment:

```bash
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

###  Step 4: Install dependencies

```bash
pip install -r requirements.txt

###  Step 5: Set up environment variables

Example .env file:
# .env

SECRET_KEY='django-insecure-7tfrb&=mdi2!jj#9p7wargu6+tn0ni*r@r2-^p(90fz)vlht+z'
DEBUG=True

# Database credentials
DB_NAME=smalltskdb
DB_USER=postgres
DB_PASSWORD=********
DB_HOST=localhost
DB_PORT=5432

# Email settings
EMAIL_PORT=587

api_key ='******************************************************'

MAILERSEND_API_KEY="********************************"

### Step 6: Apply migrations

```bash
python manage.py migrate

### Step 7: Create a superuser (optional)

```bash
python manage.py createsuperuser

### Step 8: Run the development server

```bash
python manage.py runserver



