# test-task

Задача: Используя докер-образ ... как основу, развернуть веб-приложение в яндекс-облаке.
 
Решение: 
Создано приложение на python, разворачивается на виртуальной машине в яндекс-облаке под ОС Ubuntu.

Скрипт для установки и код программы папке test.

Для настройки поднимаем  виртульный сервер яндекс-облаке под ОС Ubuntu.

Клонируем репозиторий

 git clone https://github.com/vnbtest/test-task
 
Заходим в папку 
 
 cd ~/test-task/test
 
 Запускаем скрипт
 
 bash install_docker_ubuntu.sh
 
 Для тестирования приложений используем localhost , либо ip адрес сервера 
 
 # Docker test web-app    
  curl -u "admin":"admin" http://localhost:8080/get-time

# Docker test web-app with error  
  curl -u "admin":"admin" http://localhost:8080/get-time_error
 
 
 