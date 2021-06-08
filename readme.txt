1. Install requirement

pip install -r requirements.txt


2. Run MySQL server, run processData.sql in MySQL, load the database

3. change line 6-7 to your MySQL username and password

app.config['MYSQL_DATABASE_USER'] = your_username
app.config['MYSQL_DATABASE_PASSWORD'] = your_password

4. python app.py

use browser to broswe http://127.0.0.1:5000/