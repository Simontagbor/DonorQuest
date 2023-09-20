-- Create empty databases
CREATE DATABASE IF NOT EXISTS dev_db;
CREATE DATABASE IF NOT EXISTS test_db;

-- Create users
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev';
CREATE USER IF NOT EXISTS 'test'@'localhost' IDENTIFIED BY 'test';

-- Grant privileges to dev user on dev_db
GRANT ALL PRIVILEGES ON dev_db.* TO 'dev'@'localhost' WITH GRANT OPTION;

-- Grant privileges to test user on test_db
GRANT ALL PRIVILEGES ON test_db.* TO 'test'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
