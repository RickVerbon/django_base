PROJECT_NAME = base
DOCKER_EXEC = docker exec -it
DOCKER_COMPOSE = docker-compose
APP = app

factory-reset:
	$(MAKE) clean
	$(MAKE) build
	$(MAKE) up
	$(MAKE) migrations
	$(MAKE) migrate

stop:
	$(DOCKER_COMPOSE) down

clean: down
	$(DOCKER_COMPOSE) down -t 0 -v --remove-orphans

restart:
	$(DOCKER_COMPOSE) restart

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

migrations:
	$(DOCKER_EXEC) $(APP) python3 manage.py makemigrations

migrate:
	$(DOCKER_EXEC) $(APP) python3 manage.py migrate

loaddata:
	$(DOCKER_EXEC) $(APP) python3 manage.py loaddata default.json

tail:
	docker logs --tail 0 --follow $(APP)

superuser:
	$(DOCKER_EXEC) $(APP) python3 manage.py createsuperuser --email admin@localhost --username admin

bash:
	$(DOCKER_EXEC) $(APP) $(APP) bash

test:
	$(DOCKER_EXEC) $(APP) python3 manage.py test
