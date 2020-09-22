Allows you to deploy messageboardapp with 3 basic commands to either docker or kubernetes:  

1.  docker-compose up -d --build (builds the images and deploys them in a pure docker environment)
2.  docker stack deploy -c docker-compose.yml messageboardapp-stack  (deploys existing images to a kubernetes environment using the docker-compose file)
3.  kubectl apply -f <yamlFileName>  (deploy existing images to a kubernetes environment using kubernetes yaml deployment files)


1. Use pertinent files in docker-compose folder: Deploy the web application in a pure docker environment with docker compose.  With the command:  'docker-compose up -d' you can spin up 3 docker containers networked with each other.  One container runs the postgres instance, one container runs the web application exposed on port 8000 via the wsgi gunicorn channel, one container runs the nginx server serving the web app on a dedicated port 1338.  This pure docker deployment with docker-compose is based off of a Dockerfile and a docker-compose yaml file.  The postgres database is accessible from outside the docker container via 5432 port.

2. Use pertinent files in docker-stack folder. Deploy the web application to a kubernetes single node cluster environment with docker-stack command.  Docker-stack will generate a full set of kubernetes deployment yaml files which cannot be reused with the kubectl apply -f <yamlfilename> command.  This means that the generated kubernetes files are read-only files and cannot be reused for manual deployment with the kubectl command.  In this scenario 3 different pods will be created in the single node kubernetes cluster.  1 pod runs the web app exposed at port 8000 via the gunicorn wsgi channel.  The web app application is accessible from outside the kubernetes cluster via port specified in the docker compose yaml file.  1 pod runs the nginx server exposing the web app on port 1338  The web application served by nginx is accessible from outside the kubernetes cluster via port specified in docker compose file.  1 pod runs the postgres database on port 5432.  The postgres database is accessible from outside the kubernetes cluster via port specified in docker compose file.  The nodePorts are allocated by docker-stack.

3. Use pertinent files in k8s folder.  Deploy the web app to a single node kubernetes cluster with kubernetes deployment yaml files.   In this scenario 3 different pods will be created.  1 pod runs the web app exposed at port 8000 via the gunicorn wsgi channel.  The web app application is accessible from outside the kubernetes cluster via NodePort 3100.  1 pod runs the nginx server exposing the web app on port 1338  The web application served by nginx is accessible from outside the kubernetes cluster via NodePort 30000.  1 pod runs the postgres database on port 5432.  The postgres database is accessible from outside the kubernetes cluster on NodePort selected:  32000.  All NodePorts are allocated in the kubernetes yaml files and maybe changed.  The range of allowable NodePorts is from 30000-32767.  Make sure to select a free port within the range.



MessageBoardapp is a simple web application that prints messages stored in the post_posts DB table to a webpage. Use URL: http://localhost:8000/ if you decide to run the MessageBoardApp using the built-in django sqlite3 webserver. (python manage.py runserver)

This application can be run in a docker container. It can be deployed and run in a kubernetes cluster as well. Instructions to run the app in a kubernetes cluster and in a docker environment are located in the documentation folder.

The app can be containerized using Dockerfile and docker-compose.yml. Use the -f option if your docker-compose file has a different name than the default one.

The MessageBoardApp uses Postgres12-alpine DB to store messages in the post_posts DB table and uses nginx to serve the home page that displays messages previously entered. To post new messages to the message board use the admin application at http://localhost:8000/admin. The admin page allows you to save/update/delete post messages.

Build the docker container images and run them using the command: docker-compose up -d --build

On a linux box, to build and run the docker-compose images, you must install the Docker engine. For centos7, use this link: https://docs.docker.com/engine/install/centos/.

Install docker-compose with the command: sudo pip install docker-compose

CD to the MessageBoardApp top directory where manage.py is located and run the command to build and run the docker-compose image:

docker-compose up -d --build

Since the docker-compose.yml file exposes the nginx port 1338:80, access the MessageBoardApp at: http://localhost:1338/

Access the admin app to enter messages and save them to the Postgres DB at: http://localhost:1338/admin

The admin app allows use to create messages to post. Messages are saved in the postgres database.

In a windows environment, you have several choices.  On Windows 10Pro you can use Docker-Desktop, a full blown kubernetes/docker environment.  You can also use minikube.  Instructions on how to set up DockerDesktop or minikube are in the documentation folder.
In a lower version of windows, you can use DockerToolbox and the OracleVM which holds the minikube virtual VM.


To build and run the MessageBoardApp using the docker public images login into Dockerhub (https://hub.docker.com/) and download the web image from the repository:

monicamarshall/messageboardproject_web
You can also open a terminal on your linux box, login into dockerhub using the command: docker login -u , enter you password, Then issue the docker pull command to download the MessageBoarddApp image. Then use the command: docker-compose up to run the image:

docker pull monicamarshall/messageboardproject_web:v1.0
docker-compose up -d --build
The documents in the Documentation folder will walk you through building the images from source code and deploying the images to Docker and to Kubernetes.
