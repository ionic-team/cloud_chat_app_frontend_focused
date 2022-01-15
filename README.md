# Chat app wireframe

## Notes before you start
This app is functional but not complete: there are missing feature and the code style is far from perfect. 

We chose to use Python and React because these are part of our stack, but you can use anything you want.

This is mostly an example to help you getting started with docker and not spend too much time setting up
the base project. 

Feel free to use this as baseline for your project, as a reference or discard it completely.


## Getting Started

### Prerequisites

- Make sure to have [docker](https://docs.docker.com/get-docker/) installed beforehand

### Running app

```shell
docker-compose up

# or run in daemon mode

docker-compose up -d
```

The first run will also build the containers.

After the first run you need to run the first existing migrations
```shell
docker-compose run api alembic upgrade head
```

The API should be available at `http://localhost:5000`

The UI should be available at `http://localhost:3000`

The code in API and UI is mounted directly inside the container and the API app is running with auto reloading,
meaning you do not need to rebuild the containers if you just modify the code.

If you add libraries to the UI or to the API, you need to rebuild the containers to install them.
This is quite obvious for the API (being a python project) but not for the UI, considering 
the `node_modules` is created inside the container in the same directory where the source code is 
but ut is not shared with mounted directory on the host machine. 


### Note about the API
There are few routes already implemented: 
- `/user`
- `/room`
- `/room/<room_id>/message`

Each allows to crete an object, list all the objects or get a single one. 


### Stopping app
```shell
docker-compose down -v
```
Note: the `-v` is important because of the named volume defined for the UI project.

### Running database migrations

```shell
docker-compose run api alembic upgrade head
```

### Autogenerate new database migrations

```shell
docker-compose run api alembic revision --autogenerate -m "New table or something"
```

### Downgrade database migration

```shell

# Downgrade most recent migration
docker-compose run api alembic downgrade -1

# Downgrade to a specific revision
docker-compose run api alembic downgrade <HASH>
```
