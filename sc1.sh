sudo apt install apache2
sudo apt install ufw
sudo ufw enable
sudo ufw app list
sudo ufw allow 'Apache Full'
sudo ufw allow 'OpenSSH'
sudo apt install mysql-server
sudo mysql_secure_installation
sudo apt install php libapache2-mod-php php-mysql
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';