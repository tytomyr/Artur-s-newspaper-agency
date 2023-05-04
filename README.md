# Artur-s-newspaper-agency"
### Installation

Clone the repository by running the following command:
`git clone https://github.com/tytomyr/Artur-s-newspaper-agency`
- Install virtual environment: 
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
```
- Install the required packages by running:
`pip install -r requirements.txt`
- Set the required environment variables in .env 
- Run node.js 
```
npm init -y
npm install http-server
npm install live-server
npm install lite-server
```
- Apply the database migrations by running:
`python manage.py migrate`
- Install demo-objects
`python manage.py loaddata newspaper_agency_db_data.json`
- Start the development server by running:
` python manage.py runserver`


## Getting Access
To access the site, you need to create a user or use 
already existing credentials
```
- Login: `admin.user`
- Password: `1qazcde3`
```
