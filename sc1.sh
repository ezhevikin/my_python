sudo apt -y install tasksel
sudo tasksel install lamp-server
sudo apt -y install ufw
sudo ufw enable
sudo ufw app list
sudo ufw allow 'Apache Full'
sudo ufw allow 'OpenSSH'
sudo apt -y install php libapache2-mod-php php-mysql
sudo apt -y install phpmyadmin
sudo mysql
#sudo mysql -u root -p << EOF
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '99Enagih/';
exit
EOF