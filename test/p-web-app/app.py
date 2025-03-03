from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()

# Настройка пользователей и паролей
users = {
    "admin": "admin",  # Логин: admin, Пароль: secretpassword
    "user": "user"      # Логин: user, Пароль: userpassword
}

# Путь к shell-скрипту
SCRIPT_PATH = "./get_time.sh"

# Функция проверки аутентификации
@auth.verify_password
def verify_password(username, password):
   if username in users and users[username] == password:
      return username

@app.route('/get-time', methods=['GET'])
@auth.login_required  # Требуется аутентификация
def get_time():
    try:
        # Выполнение shell-скрипта
        result = subprocess.run(SCRIPT_PATH, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Возвращаем результат с HTTP-статусом 200
        return jsonify({"status": "success", "result": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        # В случае ошибки возвращаем HTTP-статус 500
        return jsonify({"status": "error", "message": str(e.stderr)}), 500

# Путь к shell-скрипту
SCRIPT_PATH1 = "./get_time1.sh"

@app.route('/get-time_error', methods=['GET'])
@auth.login_required  # Требуется аутентификация
def get_time_error():
    try:
        # Выполнение shell-скрипта
        result = subprocess.run(SCRIPT_PATH1, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Возвращаем результат с HTTP-статусом 200
        return jsonify({"status": "success", "result": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        # В случае ошибки возвращаем HTTP-статус 500
        return jsonify({"status": "error", "message": str(e.stderr)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
