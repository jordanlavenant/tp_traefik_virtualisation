FROM php:7.4-apache

# Install mysqli extension
RUN docker-php-ext-install mysqli
RUN pecl install redis && docker-php-ext-enable redis