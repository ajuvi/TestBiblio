SET NAMES utf8mb4;

CREATE DATABASE IF NOT EXISTS db_biblio
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE db_biblio;

CREATE TABLE IF NOT EXISTS Llibre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titol VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    any_publicacio INT,
    disponible TINYINT(1) DEFAULT 1
);

INSERT INTO Llibre (titol, autor, any_publicacio, disponible) VALUES
    ('El petit príncep', 'Antoine de Saint-Exupéry', 1943, 1),
    ('Harry Potter i la pedra filosofal', 'J. K. Rowling', 1997, 1),
    ('Harry Potter i la cambra secreta', 'J. K. Rowling', 1998, 1),
    ('El Hobbit', 'J. R. R. Tolkien', 1937, 1),
    ('Matilda', 'Roald Dahl', 1988, 1),
    ('Wonder', 'R. J. Palacio', 2012, 1),
    ('Percy Jackson i el lladre del llamp', 'Rick Riordan', 2005, 1),
    ('El diari de Greg', 'Jeff Kinney', 2007, 1);