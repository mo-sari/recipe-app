# recipe-app-api
## steps before creation of the first commit
1- generate a token from dockerhub
2- create two github secrets, one for username and the second for dockertoken

## docker-compose 
Instead of running additional commands before starting your container, you can define the command directly within the docker-compose.yml file for each service. This way, docker-compose up will automatically build and run the container with your specified command, streamlining the process