# Django Base

## Introduction

This project serves as a comprehensive starting point / blueprint for launching a new Django project quickly and efficiently. You can jumpstart your development process without having to repeat common setup tasks and configurations for every new project.

## Why Django Base?

Django Base was created to streamline the initial setup and configuration process for new Django projects. As a developer, I often found myself spending valuable time on repetitive tasks such as setting up authentication systems, integrating databases, configuring Docker environments, and implementing basic testing frameworks. With Django Base, all of these foundational elements are pre-configured and ready to go, allowing you to focus on building and iterating on your unique project ideas.

## Features

- **Django Backend with Docker Setup**: Start with a robust Django backend environment configured to run seamlessly within Docker containers.
- **PostgreSQL Database Integration**: Utilize PostgreSQL as the database engine for your projects, ensuring reliability and scalability.
- **Authentication and User Management**: Leverage the pre-built users app for easy implementation of authentication and user management functionalities.
- **Integration with Mailpit**: Seamlessly integrate Mailpit for testing email communications within your Django projects.
- **Django Debug Toolbar:** Gain valuable insights into your project's performance and behavior during development with the Django Debug Toolbar.
- **Flake8 Configuration**: Ensure code quality and reliability with basic tests for the user app and adherence to PEP 8 standards using Flake8.

## What's Included

This project blueprint includes everything you need to kickstart your Django projects, including:

- Pre-configured Django project structure with modular apps
- Docker and Docker Compose setup for local development and deployment
- Configuration files for development, testing, and production environments
- Ready-to-use templates for common Django components (views, models, forms, etc.)
- Documentation and README template for easy project setup and onboarding

# Getting Started

Follow these steps to set up and run your Django project using Django base:

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your local machine:
- Docker
- Docker Compose

## Installation
Clone the repository to your local machine:
```python
git clone https://github.com/RickVerbon/django_base.git
```

Build and start the Docker containers using Docker Compose:
```python
docker-compose up -d --build 
```
*Note:* There is a Makefile included in the project. If you use Linux or WSL and have ```make``` installed, you can use ```make factory-reset``` to build the project

Once the containers are up and running, you can access your Django project at http://localhost:8000.


## Testing

To run the basic tests included in the project, execute the following command:
```docker-compose run app python manage.py test```

*Note*: When using ```make``` as you could run ```make test```

## Access django container
You can access the app container by running ```docker exec -it app bash``` 

From there you can also run normal commands like:
```python3 manage.py test``` or ```python3 manage.py migrate```
