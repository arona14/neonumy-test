# Neonumy Photo Album

A modern photo album application built with Django that allows users to upload, view, and manage images with a clean and responsive interface.

## Features

- Image upload with title
- Gallery view with responsive grid layout
- Image detail view
- Delete functionality
- GraphQL API support
- Modern and clean UI
- Responsive design

## Tech Stack

- Python 3.12+
- Django 5.1+
- PostgreSQL
- GraphQL (Graphene-Django)
- HTML5/CSS3
- Poetry (Package Management)

## Prerequisites

- Python 3.12 or higher
- PostgreSQL
- Poetry (Python package manager)
- Docker (optional)

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd neonumy_album
```

2. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Activate the virtual environment:
```bash
poetry shell
```

5. Create a PostgreSQL database:
```sql
CREATE DATABASE neonumy_album;
```

6. Update database settings in `neonumy_album/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neonumy_album',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

7. Run migrations:
```bash
poetry run python manage.py migrate
```

8. Create a superuser (optional):
```bash
poetry run python manage.py createsuperuser
```

9. Start the development server:
```bash
poetry run python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Docker Setup

1. Build the Docker image:
```bash
docker build -t neonumy-album .
```

2. Run with Docker Compose:
```bash
docker-compose up
```

## API Documentation

### GraphQL API

The application provides a GraphQL API endpoint at `/graphql/`. You can use the GraphiQL interface in development mode to explore the API.

#### Available Queries

```graphql
# Get all images
query {
  allImages {
    id
    title
    image
  }
}

# Get single image
query {
  image(id: "1") {
    id
    title
    image
  }
}
```

#### Available Mutations

```graphql
# Upload image
mutation {
  uploadImage(title: "My Image", image: Upload!) {
    image {
      id
      title
      image
    }
  }
}

# Delete image
mutation {
  deleteImage(id: "1") {
    success
  }
}
```

## Project Structure

```
neonumy_album/
├── images/                 # Main application
│   ├── static/            # Static files
│   │   └── images/        # CSS and other assets
│   ├── templates/         # HTML templates
│   │   └── images/        # Application templates
│   ├── models.py          # Database models
│   ├── views.py           # View controllers
│   └── schema.py          # GraphQL schema
├── neonumy_album/         # Project settings
├── media/                 # Uploaded media files
├── staticfiles/           # Collected static files
├── manage.py             # Django management script
├── pyproject.toml        # Poetry configuration
├── poetry.lock          # Poetry lock file
├── Dockerfile           # Docker configuration
└── docker-compose.yml   # Docker Compose configuration
```

## Development

### Running Tests
```bash
poetry run python manage.py test
```

### Code Style
The project follows PEP 8 style guide. You can check and format the code using:
```bash
# Run flake8 for code style checking
poetry run flake8 .

# Run black for code formatting
poetry run black .
```

## Deployment

### Production Settings

1. Update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
```

2. Configure static files:
```bash
poetry run python manage.py collectstatic
```

3. Set up a proper web server (e.g., Nginx) and WSGI server (e.g., Gunicorn).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 