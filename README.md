# eda2da — Кулинарный помощник

Веб-приложение для поиска рецептов по ингредиентам, планирования питания и генерации списков покупок.

**Стек:** React + Django REST Framework + PostgreSQL  
**Методология:** Scrum (5 спринтов по 2 недели)  
**Документация:** [GitHub Wiki](../../wiki)

---

## Быстрый старт (Docker Compose)

### Требования

- Docker >= 24.0
- Docker Compose >= 2.0

### Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/<org>/eda2da.git
cd eda2da

# 2. Скопировать и заполнить переменные окружения
cp .env.example .env

# 3. Поднять все сервисы
docker compose up --build
```

Приложение будет доступно по адресам:

| Сервис | URL |
|--------|-----|
| Frontend (React) | http://localhost:5173 |
| Backend API | http://localhost:8000/api/ |
| Swagger UI | http://localhost:8000/api/schema/swagger-ui/ |
| pgAdmin | http://localhost:5050 |

---

## Переменные окружения

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

## Структура репозитория

```
eda2da/
├── frontend/               # React + Vite (JavaScript)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── api/
│   ├── package.json
│   └── vite.config.js
├── backend/                # Python 3.12 / Django REST Framework
│   ├── recipes/            # Модели Recipe, Ingredient
│   ├── users/              # Модели User, Subscription
│   ├── mealplan/           # Модель MealPlan
│   ├── config/             # settings.py, urls.py
│   ├── requirements.txt
│   └── manage.py
├── db/                     # Миграции PostgreSQL, ERD-схемы
│   └── erd.png
├── docs/                   # ТЗ, диаграммы, Sphinx-документация
│   └── source/
├── .github/
│   └── workflows/
│       ├── backend.yml     # CI: pytest + pylint
│       └── frontend.yml    # CI: Jest + ESLint
├── docker-compose.yml
├── .env.example
├── CHANGELOG.md
└── README.md
```

---

## Запуск без Docker

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

## Тестирование

```bash
# Backend (pytest)
cd backend
pytest --cov=. --cov-report=term-missing

# Frontend (Jest)
cd frontend
npm test
```

---

## Стратегия ветвления (Git Flow)

| Ветка | Назначение |
|-------|-----------|
| `main` | Стабильная production-ветка |
| `develop` | Основная ветка разработки |
| `feature/sprint-N-<name>` | Задачи спринта |
| `hotfix/<description>` | Срочные исправления в production |

Все изменения вносятся через **Pull Request** с code review минимум от одного участника.  
Commit-сообщения: `feat:`, `fix:`, `docs:`, `test:`, `refactor:` ([Conventional Commits](https://www.conventionalcommits.org/)).

---

## Команда (группа ИКБО-63-23)

| Роль | Участник |
|------|---------|
| Product Owner / Аналитик | Поспелов Д.Д. |
| Scrum Master / Тестировщик | Жулёв Е.А. |
| Frontend / Backend разработчик | Оганнисян Н.Г. |
| Backend / Технический писатель | Головач Н.Е. |
