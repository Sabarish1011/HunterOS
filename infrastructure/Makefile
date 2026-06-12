.PHONY: up down logs ps build restart clean data-up

COMPOSE = docker compose -f docker-compose.yml

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

ps:
	$(COMPOSE) ps

build:
	$(COMPOSE) build

restart:
	$(COMPOSE) restart

clean:
	$(COMPOSE) down -v

data-up:
	$(COMPOSE) up -d postgres redis qdrant
