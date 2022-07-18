# Solution for the CybSafe Django Challenge

## Everything works within docker containers, managed by docker-compose.

Steps to build:

1. run `make compose_up` (or `make compose_rebuild` if you already have running compose)
2. wait for couple of seconds to let postgres up
3. run `make compose_migrate` which will create necessary tables in postgres
4. run `make compose_createsuperuser` to create root user for Django admin
5. run `make compose_crawl_remote_api` to populate database with Pokemon data from api  
6. open Django admin on http://127.0.0.1:8000/admin/ to see Pokemon data
