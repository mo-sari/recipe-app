# recipe-app-api

## steps before creation of the first commit

1- generate a token from dockerhub
2- create two github secrets, one for username and the second for dockertoken

## docker-compose

Instead of running additional commands before starting your container, you can define the command directly within the docker-compose.yml file for each service. This way, docker-compose up will automatically build and run the container with your specified command, streamlining the process

## Linting

if we run docker-compose the DEV is equal to true which means we're going to
install flake8 but if we only because in docker-compose we're overriding the
DEV arg in dockerfile itself.
changed the docker-compose and dockerfile and then ==> docker-compose build
add .flake8 file to configure flake8 package
docker-compose run --rm app sh -c "flake8" ==> Linting

## Creating the Django Project

docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose up

## Fixing db race condition

docker-compse run --rm app sh -c "python manage.py startapp core"
Implement management commands

## Changes needed for CI/CD

first update the workflow
run docker-compose down
docker-compose up (you should see "Waiting for database" and "Database available" in terminal)

## Configure django user model

first create the model and model manager classes
configure the settings file to use our custom user model
run migrations( make migrations)
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
(with previous command running you should get an error because we have ran the migrations
before and we have created a user model in our database)
(for previously mentioned problem we can inspect volumes and delete the volume which was
connected to our database)
docker volume ls
docker volume rm <volume_name>
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

## Creating a new superuser

(run docker-compose up to see if everything is ok)
docker-compose run --rm app sh -c "python manage.py createsuperuser"
in running app go to admin panel and enter using super_user credentials

## Creating the api schema

(update the requirements.txt and then ==>)
docker-compose build
then configure settings.py
then configure urls.py

## UserAPI

docker-compose run --rm app sh -c "python manage.py startapp user"
(remove migrations, admin, models.py, tests.py)
(create a new directory for tests, in it create **init**)
add user to Installed_apps
implement the tests(test_user_api.py)
(skipped this part)

## RecipeAPI

one good example of why would we use get_serializer_class method in a view

## Required system libraries

when working with containerized app's we choose an OS, and that might not have
some basic needed libraries by default ( like we need to work with images but
our OS does not support that out of the box so we would have to install some
stuff on it). those libraries we must find based on our OS, that are they needed
or does the python package I'm about to install need any of those libraries?
then we would install them in our dockerfile using apk
(now that we want to use pillow we need some system and python packages as well
and we installed them all)
then run docker-compose build

## Configuration of static and media files

update dockerfile
docker-compose build
update docker-compose
update settings file
