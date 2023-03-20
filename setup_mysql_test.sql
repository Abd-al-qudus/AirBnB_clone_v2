-- a script that creates the test db for airbnb sql server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user with username hbnb_test with password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
