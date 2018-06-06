# docker_web_mongo
a project using docker and mongodb

example usage(in ubuntu enviroment)
start container in local:
cd docker_web_mongo
sudo docker-compose up

then type in browser to save (key1,value1) in database:
http://0.0.0.0:5000/v1/key/key1/value/value1

type in browser  http://0.0.0.0:5000/v1/key/key1 to get the value corresponding to key1



close container:
sudo docker-compose up
