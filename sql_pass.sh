#! /bin/bash
sudo mysql -u root -p << EOF
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '99Enagih/';
exit
EOF