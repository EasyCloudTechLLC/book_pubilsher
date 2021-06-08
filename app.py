from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'bookPublisher'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list_authors', methods=['POST', 'GET'])
def list_authors():

    cursor = mysql.connect().cursor()

    cursor.execute("SELECT * FROM authors")
    data = cursor.fetchall()

    cursor.close()
    return render_template('list_authors.html',data = data)

@app.route('/list_publishers', methods=['POST', 'GET'])
def list_publishers():

    cursor = mysql.connect().cursor()

    cursor.execute("SELECT * FROM publishers")
    data = cursor.fetchall()

    cursor.close()
    return render_template('list_publishers.html',data = data)


@app.route('/list_books', methods=['POST', 'GET'])
def list_books():

    cursor = mysql.connect().cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()

    cursor.close()
    return render_template('list_books.html',data = data)


@app.route('/list_book_author', methods=['POST', 'GET'])
def list_book_author():

    cursor = mysql.connect().cursor()

    cursor.execute("select a.authorID, a.firstName, a.lastName, ba.bookID, b.publisherID, b.isbn, b.title, b.price, b.edition, b.copyright, b.pages from authors a, books b, book_author ba where a.authorID=ba.authorID and b.bookID=ba.bookID")
    data = cursor.fetchall()

    cursor.close()
    return render_template('list_book_author.html',data = data)

@app.route('/get_books_from_author', methods=['POST', 'GET'])
def get_books_from_author():
    return render_template('get_books_from_author.html')

@app.route('/result_get_books_from_author', methods=['POST', 'GET'])
def result_get_books_from_author():
    if request.method == 'POST':
        authorName = request.form['authorName']

        cursor = mysql.connect().cursor()

        cursor.execute(
            f"select a.authorID, a.firstName, a.lastName, ba.bookID, b.publisherID, b.isbn, b.title, b.price, b.edition, b.copyright, b.pages from authors a, books b, book_author ba where a.authorID=ba.authorID and b.bookID=ba.bookID and (a.firstName like CONCAT('%', '{authorName}', '%') or a.lastName like CONCAT('%', '{authorName}', '%'))")
        data = cursor.fetchall()

        cursor.close()
        return render_template('result_get_books_from_author.html',data=data)

@app.route('/get_books_from_publisher', methods=['POST', 'GET'])
def get_books_from_publisher():
    return render_template('get_books_from_publisher.html')

@app.route('/result_get_books_from_publisher', methods=['POST', 'GET'])
def result_get_books_from_publisher():
    if request.method == 'POST':
        publisherName = request.form['publisherName']

        cursor = mysql.connect().cursor()

        cursor.execute(
            f"select p.publisherID, p.publisherName, b.bookID, b.isbn, b.title, b.price, b.edition, b.copyright, b.pages from publishers p, books b where p.publisherID=b.publisherID and p.publisherName like CONCAT('%', '{publisherName}', '%')")
        data = cursor.fetchall()

        cursor.close()
        return render_template('result_get_books_from_publisher.html',data=data)


@app.route('/insert_author', methods=['POST', 'GET'])
def insert_author():
    return render_template('insert_author.html')

@app.route('/process_insert_author', methods=['POST', 'GET'])
def process_insert_author():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            f"INSERT INTO authors(firstName, lastName) VALUES('{firstName}','{lastName}')")
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('success.html')

if __name__ == '__main__':
    app.run()
