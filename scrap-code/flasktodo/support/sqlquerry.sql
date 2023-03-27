-- PostgreSQL
CREATE TABLE todo(
id SERIAL PRIMARY KEY,
title VARCHAR(30) NOT NULL,
content VARCHAR(255) NOT NULL);

-- Mariadb
CREATE TABLE todo (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(30) NOT NULL,
  content VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
