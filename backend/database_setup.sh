#!/bin/bash

# Database configurations
DB_NAME_DEV="dev_db"
DB_USER_DEV="dev"
DB_PASSWORD_DEV="dev"

DB_NAME_TEST="test_db"
DB_USER_TEST="test"
DB_PASSWORD_TEST="test"

# Create databases and users with sudo
sudo mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $DB_NAME_DEV;"
sudo mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $DB_NAME_TEST;"
sudo mysql -u root -p -e "CREATE USER IF NOT EXISTS '$DB_USER_DEV'@'localhost' IDENTIFIED BY '$DB_PASSWORD_DEV';"
sudo mysql -u root -p -e "CREATE USER IF NOT EXISTS '$DB_USER_TEST'@'localhost' IDENTIFIED BY '$DB_PASSWORD_TEST';"

# Grant privileges with sudo
sudo mysql -u root -p -e "GRANT ALL PRIVILEGES ON $DB_NAME_DEV.* TO '$DB_USER_DEV'@'localhost';"
sudo mysql -u root -p -e "GRANT PROCESS PRIVILEGES ON $DB_NAME_DEV.* TO '$DB_USER_DEV'@'localhost';"
sudo mysql -u root -p -e "GRANT ALL PRIVILEGES ON $DB_NAME_TEST.* TO '$DB_USER_TEST'@'localhost';"
sudo mysql -u root -p -e "FLUSH PRIVILEGES;"

# # Import SQL dump file into the dev database (if not already initialized)
# if ! mysql -u "$DB_USER_DEV" -p"$DB_PASSWORD_DEV" -e "use $DB_NAME_DEV"; then
#     mysql -u "$DB_USER_DEV" -p"$DB_PASSWORD_DEV" "$DB_NAME_DEV" < /app/dev_dbdump.sql
#     echo "Dummy data imported."
# else
#     echo "Database already initialized, skipping import."
# fi


echo "Databases and users created successfully."

