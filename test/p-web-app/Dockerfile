FROM genotek/r-base

# Скопируем API-скрипт
COPY app.py get_time.sh /app/

# Установим рабочую директорию
WORKDIR /app

# Установка зависимостей
RUN apt-get update && apt-get install -y python3-pip \
   && pip3 install flask flask-httpauth \
   && mkdir -p ~/app \
   && chmod +x get_time.sh

# Порт для Flask
EXPOSE 5000

# Команда для запуска
CMD ["python3", "app.py"]


