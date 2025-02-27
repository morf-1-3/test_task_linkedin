LinkedIn Profile Picture Scraper

📌 Опис

Цей скрипт автоматизує вхід у LinkedIn та завантажує фото профілю користувача. Всі логи зберігаються у файлі out.log. Виконується всередині Docker-контейнера.

🚀 Як запустити

1️⃣ Створити .env файл у кореневій папці проєкту

Заповніть його своїми обліковими даними:

LOGIN=your_email_or_phone
PASS=your_password

2️⃣ Зібрати Docker-образ

docker build -t my_app .

3️⃣ Запустити контейнер з використанням .env

docker run --env-file .env my_app

📂 Логи

Всі логи записуються у out.log.

🔹 Використані технології

Python + Selenium + urllib

Docker
