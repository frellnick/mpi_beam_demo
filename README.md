# MPI Beam Demo System
Port of MPI Demo system to Apache Beam components

## Mock Ingest
Load data from local files or test database as if they'd been ingested.

Controlled by ENVIRONMENT in settings.ini:
* DEV - read from local csv
* STAGING - Not Implemented (staging_database)
* PRODUCTION - Not Implemented (production_database)

## MPI
Exposes API for processing ingested tables

## DI
Exposes API to de-identify a table



### Starting Databases with Docker or Podman

MPI NoSQL demos require a configured MongoDB instance.

Setting up MongoDB
1. Start MongoDB container

> podman run -d --name mongo_db -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=dbpassword mongo

2. Enter the container and create a collection

> podman exec -it mongo_db bash

3. Create application Role and DB (or skip and use root stuff for testing)

> XXXX


## Tests

Tests written with pytest

Run all tests with:

```bash
pytest
```

### Managing Conda Environments & Runners

**Create** cloned environment with

```bash
conda env create -f environment.yml
```

**Update** environment.yml with 

```bash
conda env export > environment.yml
```

* Check that pip dependencies written in.
* Delete prefix at end of file (won't work across users, OS)

**Runners** require a 'requirements.txt' file.  Create with:
```bash
pip freeze > requirements.txt
```
* Ensure that all packages are pypy packages, else runners will not be able to install



### Creating PipEnv shell

You can create a pipenv shell from environment.yml via:

1. Steps (probably want a requirements.txt or something)