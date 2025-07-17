# quote_api
Microservice for storing and searching quotes using FastAPI
Це мікросервіс для зберігання, створення та пошуку цитат. Створено з використанням FastAPI.

 #Функціонал
- Додавання цитат
- Пошук за ID
- Отримання списку з пагінацією
- Оновлення цитат
- Видалення цитат

#Запуск локально
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
