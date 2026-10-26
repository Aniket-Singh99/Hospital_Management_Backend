# Healthcare Backend

Django + DRF + PostgreSQL + JWT (simplejwt).

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env            # then fill in your values
```

Create the database in PostgreSQL:

```sql
CREATE DATABASE healthcare_db;
```

Run migrations and start the server:

```bash
python manage.py makemigrations accounts patients doctors mappings
python manage.py migrate
python manage.py runserver
```

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/auth/register/ | Register (name, email, password) |
| POST | /api/auth/login/ | Login, returns access + refresh token |
| POST | /api/auth/token/refresh/ | Get new access token |
| POST/GET | /api/patients/ | Add / list your patients |
| GET/PUT/DELETE | /api/patients/<id>/ | Patient details / update / delete |
| POST/GET | /api/doctors/ | Add / list all doctors |
| GET/PUT/DELETE | /api/doctors/<id>/ | Doctor details / update / delete |
| POST/GET | /api/mappings/ | Assign doctor to patient / list mappings |
| GET | /api/mappings/<patient_id>/ | Doctors of a patient |
| DELETE | /api/mappings/<id>/ | Remove a doctor from a patient |

Send the token in the header for all endpoints except register/login:

```
Authorization: Bearer <access_token>
```

## Sample requests

Register:
```json
{ "name": "Rahul", "email": "rahul@example.com", "password": "Test@12345" }
```

Add patient:
```json
{ "name": "Amit Sharma", "age": 35, "gender": "M", "phone": "9876543210", "address": "Jaipur", "medical_history": "Diabetes" }
```

Add doctor:
```json
{ "name": "Priya Verma", "specialization": "Cardiology", "email": "priya@hospital.com", "phone": "9123456780", "experience_years": 10 }
```

Assign doctor:
```json
{ "patient": 1, "doctor": 1 }
```
