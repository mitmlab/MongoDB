-- CREATE DATABASE MOVIE_DB;
-- USE MOVIE_DB;

-- CREATE TABLE ACTOR(
-- Act_id INT PRIMARY KEY,
-- Act_Name VARCHAR(30),
-- Act_Gender VARCHAR(10)
-- );
-- DESC ACTOR; 

-- CREATE TABLE DIRECTOR(
-- Dir_id INT PRIMARY KEY,
-- Dir_Name VARCHAR(30),
-- Dir_Phone VARCHAR(15)
-- );
-- DESC DIRECTOR;

-- CREATE TABLE MOVIES(
-- Mov_id INT PRIMARY KEY,
-- Mov_Title VARCHAR(40),
-- Mov_Year INT,
-- Mov_Lang VARCHAR(20),
-- Dir_id INT,
-- FOREIGN KEY (Dir_id) REFERENCES DIRECTOR(Dir_id)
-- );
-- DESC MOVIES;

-- CREATE TABLE MOVIE_CAST(
-- Act_id INT,
-- Mov_id INT,
-- Role VARCHAR(30),
-- PRIMARY KEY(Act_id,Mov_id),
-- FOREIGN KEY (Act_id) REFERENCES ACTOR(Act_id),
-- FOREIGN KEY (Mov_id) REFERENCES MOVIES(Mov_id)
-- );
-- DESC MOVIE_CAST;

-- CREATE TABLE RATING(
-- Mov_id INT,
-- Rev_Stars INT,
-- FOREIGN KEY (Mov_id) REFERENCES MOVIES(Mov_id));
-- DESC RATING;

-- INSERT INTO ACTOR VALUES
-- (1,'Rajinikanth','Male'),
-- (2,'Kamal Haasan','Male'),
-- (3,'Aishwarya Rai','Female'),
-- (4,'Trisha','Female');
-- SELECT * FROM ACTOR;

-- INSERT INTO DIRECTOR VALUES
-- (10,'Mani Rathnam','9876543210'),
-- (11,'Shankar','9876543211'),
-- (12,'Lokesh','9876543212');
-- SELECT * FROM DIRECTOR;

-- INSERT INTO MOVIES VALUES
-- (100,'Roja',1992,'Tamil',10),
-- (101,'Bombay',1995,'Tamil',10),
-- (102,'Robot',2010,'Tamil',11),
-- (103,'Sivaji',2007,'Tamil',11),
-- (104,'Future Film',2025,'Tamil',12);
-- SELECT * FROM MOVIES;

-- INSERT INTO MOVIE_CAST VALUES
-- (1,102,'Hero'),
-- (1,103,'Hero'),
-- (2,100,'Hero'),
-- (3,101,'Heroine'),
-- (3,104,'Heroine');
-- SELECT * FROM MOVIE_CAST;

-- INSERT INTO RATING VALUES
-- (100,4),
-- (101,5),
-- (102,3),
-- (103,4),
-- (104,2);
-- SELECT * FROM RATING;

-- SELECT M.Mov_Title
-- FROM MOVIES M
-- JOIN DIRECTOR D
-- ON M.Dir_id = D.Dir_id
-- WHERE D.Dir_Name = 'Mani Rathnam';

-- SELECT DISTINCT M.Mov_Title
-- FROM MOVIES M
-- JOIN MOVIE_CAST MC ON M.Mov_id = MC.Mov_id
-- WHERE MC.Act_id IN
-- (
-- SELECT Act_id
-- FROM MOVIE_CAST
-- GROUP BY Act_id
-- HAVING COUNT(Mov_id) >= 2
-- );

-- SELECT DISTINCT A.Act_Name
-- FROM ACTOR A
-- JOIN MOVIE_CAST MC1 ON A.Act_id = MC1.Act_id
-- JOIN MOVIES M1 ON MC1.Mov_id = M1.Mov_id
-- JOIN MOVIE_CAST MC2 ON A.Act_id = MC2.Act_id
-- JOIN MOVIES M2 ON MC2.Mov_id = M2.Mov_id
-- WHERE M1.Mov_Year < 2000
-- AND M2.Mov_Year > 2024;

-- SELECT M.Mov_Title, MAX(R.Rev_Stars) AS Highest_Stars
-- FROM MOVIES M
-- JOIN RATING R
-- ON M.Mov_id = R.Mov_id
-- GROUP BY M.Mov_Title
-- ORDER BY M.Mov_Title;

-- UPDATE RATING
-- SET Rev_Stars = 5
-- WHERE Mov_id IN
-- (
-- SELECT M.Mov_id
-- FROM MOVIES M
-- JOIN DIRECTOR D
-- ON M.Dir_id = D.Dir_id
-- WHERE D.Dir_Name = 'Shankar'
-- );
-- SELECT * FROM RATING;