🍴 Проект «eda2da» (Кулинарный помощник) — Backend Engine
Данный документ является техническим описанием текущего состояния проекта. Бэкенд-часть («Двигатель») полностью реализована, протестирована и готова к интеграции с фронтендом.
🏗 Архитектура и Стек технологий
Тип системы: Трёхуровневое веб-приложение (Three-Tier Architecture).
Backend: Python 3.12 + Django 5.0.
API: Django REST Framework (DRF) 3.15.
Database: PostgreSQL 16.
Containerization: Docker / Docker Compose.
Auth: JWT (JSON Web Token) через djangorestframework-simplejwt.
Documentation: Swagger UI через drf-spectacular.
📁 Структура репозитория (Monorepo)
/backend — Исходный код сервера.
/config — Глобальные настройки Django, маршрутизация API и Swagger.
/users — Управление пользователями, ролями (GUEST, USER, SUBSCRIBER, MODERATOR) и JWT.
/recipes — Модели рецептов, ингредиентов и логика масштабирования порций.
/mealplan — Логика планирования питания и агрегации списка покупок.
/frontend — Заготовка под React-приложение.
/db — Схемы базы данных (ERD).
docker-compose.yml — Оркестрация всех сервисов.
🗄 Модель данных (Database Schema)
Реализованы следующие сущности:
User (Custom Model): Расширенный профиль с полями role, is_subscriber, preferences.
Ingredient: Справочник продуктов (название, единица измерения, калорийность, флаг аллергена).
Recipe: Заголовок рецепта (КБЖУ, сложность, время готовки, статус модерации).
RecipeComposition: Промежуточная таблица Many-to-Many между Рецептом и Ингредиентом с указанием веса (quantity).
MealPlan: План питания пользователя на диапазон дат.
MealPlanRecipe: Привязка конкретного рецепта к дате и типу приема пищи (Завтрак/Обед/Ужин).
⚙️ Ключевая бизнес-логика (Business Logic)
Масштабирование порций (scale_ingredients): Метод в модели Recipe, динамически пересчитывающий вес всех ингредиентов при изменении количества порций.
Генератор списка покупок (generate_shopping_list): Метод в модели MealPlan, который выполняет агрегацию (суммирование) всех ингредиентов из разных рецептов за выбранный период времени.
Система прав доступа:
AllowAny: Регистрация и просмотр списка проверенных рецептов.
IsAuthenticated: Управление личными планами питания и профилем.
IsAuthenticatedOrReadOnly: Создание контента (рецептов).
Admin/Moderator: Доступ к админ-панели и флагу is_moderated.
🚀 Инструкция по запуску для Разработчика / ИИ
Для развертывания проекта необходимо:
Создать файл .env на основе .env.example.
Запустить контейнеры:
code
Bash
docker compose up --build -d
Выполнить миграции базы данных:
code
Bash
docker compose exec backend python manage.py migrate
Создать суперпользователя:
code
Bash
docker compose exec backend python manage.py createsuperuser
📍 API Endpoints (Тестирование)
Полная интерактивная документация доступна после запуска по адресу:
👉 http://localhost:8000/api/schema/swagger-ui/
Основные маршруты:
POST /api/users/register/ — Регистрация.
POST /api/users/login/ — Получение JWT-токенов.
GET /api/recipes/recipes/ — Список всех одобренных рецептов.
GET /api/mealplan/plans/{id}/shopping_list/ — Генерация списка продуктов для плана.
Текущий статус проекта:
Бэкенд-часть полностью завершена. Все функциональные требования Практик №1–10 реализованы. Система готова к подключению фронтенд-интерфейса и реализации пользовательских сценариев.
