# imaginea pentru php si apache
FROM php:8-apache

# instalare extensii php
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/
RUN chmod +x /usr/local/bin/install-php-extensions


RUN install-php-extensions \
    gd \
    imap \
    mysqli \
    pdo_mysql \
    sockets \
    zip

# Enable Apache mods
RUN a2enmod headers
RUN a2enmod rewrite

# Restart Apache
RUN service apache2 restart
