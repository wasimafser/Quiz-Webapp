# Quiz-Webapp

A basic Quiz app developed in Django.
___

### Tech-Stack
* Backend:
  * Django
* Frontend:
  * HTML / JS 
* Deployment:
  * Docker / Docker-compose

### Requirements
- Docker / Docker-compose
- (or)
- Python, Django, requests, Sqlite3

### Installation
- Open up a terminal / cmd in the project root directory
- If using Docker:
  - `docker-compose up -d`
  - visit http://127.0.0.1:8000/generate_questions/ ( to generate questions )
- If using local python install
  - CD to 'backend' directory
  - Create and activate virtual env (optional)
    - `python3 -m venv venv`
    - `source venv/bin/activate` (linux/unix)
    - `venv\Scripts\activate.bat` ( windows )
  - Install requirements: `pip install -r requirements.txt`
  - Migrate data:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
  - Create superuser ( optional )
    - `python manage.py createsuperuser`
  - Load data:
    - `python manage.py loaddata app/fixtures/all_data.json`
    -  (OR)
    - run server and visit http://127.0.0.1:8000/generate_questions/
  - Start server:
    - `python manage.py runserver`
- visit http://127.0.0.1:8000


Questions are gathered from [opentdb](https://opentdb.com/) api.