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