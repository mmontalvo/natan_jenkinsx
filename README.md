# Manning LiveProject - CI/CD with JenkinsX

In order to start working with this project we would need:

* Docker
* docker-compose


You need to clone this repository onto your machine by executing:

```bash
git clone git@github.com:mmontalvo/natan_jenkinsx.git
```
or
```bash
git clone https://github.com/mmontalvo/natan_jenkinsx.git
```

After this, you go into `natan_jenkinsx` folder and run:

```bash
docker-compose up
```

It will start pulling the images needed, setting up the Postgres database installation and the packages from the Django applications.

Once both apps and the database are running, we would need to create the database and run migrations.
For it, we need to get into the database Docker running instance.

Running `docker ps` we can spot the instance running our database (it would be something similar to the following line):

```bash
_postgres-container-id_   postgres:9.6.15  "docker-entrypoint.s…"   2 days ago          Up 11 seconds       0.0.0.0:32777->5432/tcp   postgresql_1
```

Now we need to start an interactive shell, login as `postgres` user in our database and create our database with the following commands:

```bash
# Access the container where we have our database running with:
docker exec -it _postgres-container-id_ bash

# then login into our database with the default postgreSQL user:
psql -U postgres

# Within postgreSQL, we just need to create our database with the following command:
CREATE DATABASE moneyfx;

# and lastly, exit postgres interactive shell:
\q
```

Last part requires getting into each of our services and run the migrations.
We need to get first into `trading` service:
```bash
docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
_trading_id_        trading             "gunicorn --chdir re…"   2 days ago          Up 10 seconds       0.0.0.0:8100->8100/tcp    trading_1

docker exec -it _trading_id_ bash

cd rest_django_trading

python manage.py migrate
```

And then the same with `payments` service

We can verify everything is running as expected by opening a browser and point to any:
trading service: `http://localhost:8100/`
or
payments service: `http://localhost:8200/`
