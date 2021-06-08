CREATE DATABASE IF NOT EXISTS bookPublisher;

USE bookPublisher;

CREATE TABLE IF NOT EXISTS
authors(
    authorID INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    PRIMARY KEY (authorID)
);

CREATE TABLE IF NOT EXISTS
publishers(
    publisherID INT NOT NULL AUTO_INCREMENT,
    publisherName VARCHAR(100) NOT NULL,
    PRIMARY KEY (publisherID)
);

CREATE TABLE IF NOT EXISTS
books(
    bookID INT NOT NULL AUTO_INCREMENT,
    publisherID INT NOT NULL,
    isbn VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    price REAL NOT NULL,
    edition INT NOT NULL,
    copyright INT NOT NULL,
    pages INT NOT NULL,
    PRIMARY KEY (bookID),
    FOREIGN KEY (publisherID) REFERENCES publishers(publisherID) ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS
book_author(
    bookID INT NOT NULL,
    authorID INT NOT NULL,
    PRIMARY KEY (bookID, authorID),
    FOREIGN KEY (bookID) REFERENCES books(bookID) ON DELETE CASCADE,
    FOREIGN KEY (authorID) REFERENCES authors(authorID) ON DELETE CASCADE
);



INSERT INTO authors(firstName, lastName) VALUES
('Mylo','Riley'),
('Bailey','Gallagher'),
('Jonas','Saunders'),
('Marco','Kennedy'),
('Alistair','Mason'),
('Rex','Dixon'),
('Kasper','Graham'),
('Aleksander','Ward'),
('Miriam','Allen'),
('Kayden','Cook');


INSERT INTO publishers(publisherName) VALUES
('Penguin Random House'),
('MHachette Livre'),
('HarperCollins'),
('Macmillan Publishers'),
('Simon & Schuster'),
('McGraw-Hill Education'),
('Houghton Mifflin Harcourt'),
('Pearson Education'),
('Scholastic'),
('Cengage Learning');


INSERT INTO books(publisherID, isbn, title, price, edition, copyright, pages) VALUES
(1,'0131752422','How to Program',20.0,2,2008,567),
(2,'0132222205','JAVA Program',30.0,4,2018,367),
(3,'0355422421','C++ Program',40.0,5,2011,565),
(4,'0133232443','Python Program',14.0,1,2012,563),
(5,'1123732321','Scala Program',24.0,5,2018,167),
(6,'9554132434','PHP Program',22.0,3,2010,267),
(7,'1512343432','C Program',31.0,6,2009,267),
(8,'0359457321','Go Program',44.0,3,2002,563),
(9,'0485414522','Matlab Program',53.0,9,2001,563),
(10,'3323432343','Perl Program',32.0,4,2003,561),
(1,'1317535222','Visual Basic',21.0,2,1998,167),
(2,'8432222205','Visual C++',33.0,4,2001,377),
(3,'2555422421','C++ application',44.0,5,2015,595),
(4,'6133232443','Qt4 application',24.0,1,2014,574),
(5,'7123732321','Linux Program',26.0,5,2013,547),
(6,'9555462434','Linux Server',22.5,3,2017,367),
(7,'3542343432','Shell Program',31.5,6,2019,290),
(8,'5435437321','Machine Learning',43.5,3,2012,553),
(9,'3673644522','Computer Architecture',52.5,9,2011,519),
(10,'6563662343','Database',22.5,4,2013,579);


INSERT INTO book_author(bookID, authorID) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10),
(11,1),
(12,2),
(13,3),
(14,4),
(15,5),
(16,6),
(17,7),
(18,8),
(19,9),
(20,10);