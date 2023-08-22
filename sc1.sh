sudo apt -y install tasksel
sudo tasksell install lamp-server
sudo apt -y install ufw
sudo ufw enable
sudo ufw app list
sudo ufw allow 'Apache Full'
sudo ufw allow 'OpenSSH'
sudo apt -y install php libapache2-mod-php php-mysql
sudo apt -y install phpmyadmin
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
exit