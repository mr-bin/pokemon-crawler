all: requirements build

format:
	./bin/isort --profile black --filter-files ./src
	./bin/black -S -l 120 -t py310 ./src/
	./bin/flake8
	./bin/mypy --exclude='setup.py' --exclude migrations --python-version=3.10 --ignore-missing-imports -p src

requirements:
	pip install -r requirements.txt

build:
	buildout

build_dev:
	buildout -c buildout-dev.cfg

compose_all:
	make compose_rebuild; sleep 5; make compose_migrate compose_createsuperuser

createsuperuser:
	bin/manage.py createsuperuser --username root --email 1@1.co

compose_migrate:
	./bin/docker-compose exec web bash -c "bin/manage.py migrate"

compose_createsuperuser:
	./bin/docker-compose exec web bash -c "bin/manage.py createsuperuser --username root --email 1@1.co"

compose_crawl_remote_api:
	./bin/docker-compose exec web bash -c "bin/manage.py crawl_remote_api"

compose_up:
	./bin/docker-compose up --build --detach

compose_down:
	./bin/docker-compose down

compose_rebuild: compose_down compose_up
