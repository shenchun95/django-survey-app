# Django Survey Application

A web application built with Django for collecting and visualizing survey data.

## Features

- User-friendly survey form submission
- Dashboard with data visualization
- Real-time statistics display

## Setup

1. Clone the repository:
```bash
git clone https://github.com/shenchun95/django-survey-app.git
cd django-survey-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to access the application.

## Project Structure

- `main/` - Main application module
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript)
- `media/` - User uploaded files

## License

MIT License