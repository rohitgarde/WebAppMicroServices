# WebAppMicroServices

|- FlaskApp
|   |-- MyFirstFlaskApp.py
|   |-- DockerFile
|- NodeApp
|   |-- MyFirstNodeApp.js
|   |-- DockerFile
|- docker-compose.yaml
Contents of the Repository are explained below.



FlaskApp
i) MyFirstFlaskApp.py - It is a Python based Flask application which will accept Get and Post requests.
ii) DockerFile - It is a Dockerfile which contains the steps to create an image and the instructions to run it.

NodeApp
i) MyFirstFlaskNode.py - It is a Node JS application which used Express and it  will accept Get and Post requests.
ii) DockerFile - It is a Dockerfile which contains the steps to create an image and the instructions to run it.

docker-compose.yaml
i) It is a yaml file which contains the configuration of the application. With docker compose we can build and run the services defined in it with a single command.
