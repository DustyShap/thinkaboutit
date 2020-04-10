# thinkaboutit
A web based party game
Currently in development.

## Setup Instructions

* Copy the `docker.env.sample` to `docker.env` and fill in your secret values
* `docker-compose build`
* `docker-compose up -d`
*  Run `docker exec -it thinkaboutit_db_1 psql -d postgres -U postgres`, and once
   in the container run `create database thinkaboutit;`. Exit the docker shell afterwards
* Run `docker exec -it thinkaboutit_web_1 python thinkaboutit/create.py`
