# 🍴 eda2da — Кулинарный помощник

> Веб-приложение для поиска рецептов по ингредиентам, планирования питания и автоматической генерации списков покупок.

[![Stack](https://img.shields.io/badge/Stack-React%20%2B%20Django%20%2B%20PostgreSQL-blue)](#)
[![Methodology](https://img.shields.io/badge/Methodology-Scrum-orange)](#)
[![Status](https://img.shields.io/badge/Backend-Ready-success)](#)
[![Docs](https://img.shields.io/badge/Docs-GitHub%20Wiki-lightgrey)](#)

---

## 📑 Содержание

1. [О проекте](#-о-проекте)
2. [Архитектура и стек технологий](#-архитектура-и-стек-технологий)
3. [Структура репозитория](#-структура-репозитория)
4. [Модель данных](#-модель-данных)
5. [Бизнес-логика](#%EF%B8%8F-ключевая-бизнес-логика)
6. [Быстрый старт (Docker)](#-быстрый-старт-docker-compose)
7. [Запуск без Docker](#-запуск-без-docker)
8. [Переменные окружения](#-переменные-окружения)
9. [API Endpoints](#-api-endpoints)
10. [Тестирование](#-тестирование)
11. [Git Flow](#-стратегия-ветвления-git-flow)
12. [Команда](#-команда-икбо-63-23)
13. [Статус проекта](#-текущий-статус-проекта)

---

## 🎯 О проекте

**eda2da** — трёхуровневое веб-приложение, которое помогает пользователям:

- 🔍 находить рецепты по имеющимся ингредиентам;
- 📅 планировать питание на день, неделю или произвольный период;
- 🛒 автоматически формировать сводный список покупок;
- ⚖️ масштабировать порции с пересчётом веса и КБЖУ;
- 👥 разграничивать роли: гость, пользователь, подписчик, модератор.

Бэкенд-часть («Двигатель») полностью реализована, протестирована и готова к интеграции с фронтендом.

---

## 🏗 Архитектура и стек технологий

| Слой | Технология |
|------|-----------|
| **Тип системы** | Three-Tier Architecture |
| **Backend** | Python 3.12 + Django 5.0 |
| **API** | Django REST Framework 3.15 |
| **Database** | PostgreSQL 16 |
| **Containerization** | Docker / Docker Compose |
| **Auth** | JWT (`djangorestframework-simplejwt`) |
| **Documentation** | Swagger UI (`drf-spectacular`) |
| **Frontend** | React + Vite (JavaScript) |

---

## 📁 Структура репозитория

Монорепозиторий со следующим деревом:

```
eda2da/
├── frontend/                   # React + Vite (JavaScript)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── api/
│   ├── package.json
│   └── vite.config.js
│
├── backend/                    # Python 3.12 / Django REST Framework
│   ├── config/                 # settings.py, urls.py, Swagger
│   ├── users/                  # Пользователи, роли, JWT
│   ├── recipes/                # Рецепты, ингредиенты, масштабирование
│   ├── mealplan/               # Планы питания, список покупок
│   ├── requirements.txt
│   └── manage.py
│
├── db/                         # Миграции и схемы
│   └── erd.png                 # ERD-диаграмма
│
├── docs/                       # ТЗ, диаграммы, Sphinx-документация
│   └── source/
│
├── .github/
│   └── workflows/
│       ├── backend.yml         # CI: pytest + pylint
│       └── frontend.yml        # CI: Jest + ESLint
│
├── docker-compose.yml          # Оркестрация всех сервисов
├── .env.example                # Шаблон переменных окружения
├── CHANGELOG.md
└── README.md
```

---

## 🗄 Модель данных

Реализованы следующие сущности:

| Сущность | Назначение |
|----------|-----------|
| **User** *(Custom Model)* | Расширенный профиль: `role`, `is_subscriber`, `preferences` |
| **Ingredient** | Справочник продуктов: название, ед. измерения, калорийность, флаг аллергена |
| **Recipe** | Заголовок рецепта: КБЖУ, сложность, время готовки, статус модерации |
| **RecipeComposition** | Промежуточная M2M-таблица «Рецепт ↔ Ингредиент» с указанием `quantity` |
| **MealPlan** | План питания пользователя на диапазон дат |
| **MealPlanRecipe** | Привязка рецепта к дате и приёму пищи (Завтрак / Обед / Ужин) |

ERD-диаграмма доступна в `db/erd.png`.

---

## ⚙️ Ключевая бизнес-логика

### 🔢 Масштабирование порций
Метод `scale_ingredients` в модели `Recipe` динамически пересчитывает вес всех ингредиентов при изменении количества порций.

### 🛒 Генератор списка покупок
Метод `generate_shopping_list` в модели `MealPlan` агрегирует (суммирует) все ингредиенты из разных рецептов за выбранный период времени.

### 🔐 Система прав доступа

| Уровень доступа | Возможности |
|-----------------|-------------|
| `AllowAny` | Регистрация, просмотр списка проверенных рецептов |
| `IsAuthenticated` | Управление личными планами питания и профилем |
| `IsAuthenticatedOrReadOnly` | Создание контента (рецептов) |
| `Admin / Moderator` | Доступ к админ-панели, флаг `is_moderated` |

---

## 🚀 Быстрый старт (Docker Compose)

### Требования
- Docker `>= 24.0`
- Docker Compose `>= 2.0`

### Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/<org>/eda2da.git
cd eda2da

# 2. Скопировать и заполнить переменные окружения
cp .env.example .env

# 3. Поднять все сервисы
docker compose up --build -d

# 4. Применить миграции
docker compose exec backend python manage.py migrate

# 5. Создать суперпользователя
docker compose exec backend python manage.py createsuperuser
```

### Доступные сервисы

| Сервис | URL |
|--------|-----|
| 🖥 Frontend (React) | http://localhost:5173 |
| ⚙️ Backend API | http://localhost:8000/api/ |
| 📘 Swagger UI | http://localhost:8000/api/schema/swagger-ui/ |
| 🐘 pgAdmin | http://localhost:5050 |

---

## 💻 Запуск без Docker

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🔧 Переменные окружения

Скопируйте `.env.example` в `.env` и заполните значения:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL
POSTGRES_DB=eda2da
POSTGRES_USER=eda2da_user
POSTGRES_PASSWORD=your-db-password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# JWT
JWT_ACCESS_TOKEN_LIFETIME=60        # минуты
JWT_REFRESH_TOKEN_LIFETIME=7        # дни

# pgAdmin
PGADMIN_EMAIL=admin@eda2da.ru
PGADMIN_PASSWORD=admin
```

---

## 📍 API Endpoints

Полная интерактивная документация доступна после запуска по адресу:
👉 **http://localhost:8000/api/schema/swagger-ui/**

### Основные маршруты

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/api/users/register/` | Регистрация пользователя |
| `POST` | `/api/users/login/` | Получение JWT-токенов |
| `GET`  | `/api/recipes/recipes/` | Список одобренных рецептов |
| `GET`  | `/api/mealplan/plans/{id}/shopping_list/` | Генерация списка продуктов для плана |

---

## 🧪 Тестирование

```bash
# Backend (pytest)
cd backend
pytest --cov=. --cov-report=term-missing

# Frontend (Jest)
cd frontend
npm test
```

---

## 🌿 Стратегия ветвления (Git Flow)

| Ветка | Назначение |
|-------|-----------|
| `main` | Стабильная production-ветка |
| `develop` | Основная ветка разработки |
| `feature/sprint-N-<name>` | Задачи спринта |
| `hotfix/<description>` | Срочные исправления в production |

> 🔍 Все изменения вносятся через **Pull Request** с code review минимум от одного участника.
>
> 📝 Commit-сообщения: `feat:`, `fix:`, `docs:`, `test:`, `refactor:` ([Conventional Commits](https://www.conventionalcommits.org/)).

---

## 👥 Команда (ИКБО-63-23)

| Роль | Участник |
|------|---------|
| 📊 Product Owner / Аналитик | **Поспелов Д.Д.** |
| 🎯 Scrum Master / Тестировщик | **Жулёв Е.А.** |
| 💻 Frontend / Backend разработчик | **Оганнисян Н.Г.** |
| ⚙️ Backend / Технический писатель | **Головач Н.Е.** |

---

## ✅ Текущий статус проекта

> **Бэкенд-часть полностью завершена.**
> Все функциональные требования Практик №1–10 реализованы.
> Система готова к подключению фронтенд-интерфейса и реализации пользовательских сценариев.

---

<p align="center">
  <sub>Сделано с ❤️ группой Astral · РТУ МИРЭА · Scrum, 5 спринтов по 2 недели</sub>
</p>
