# docker_web_mongo
a project using docker and mongodb

example usage(in ubuntu environment):

start container in local:

cd docker_web_mongo

sudo docker-compose up


curl -H "Content-Type: application/json" -X POST "http://0.0.0.0:5000/v1" -d "key=key111&value=value111"

to save (key111,value111)

curl -X GET http://0.0.0.0:5000/v1/key/key111

to get the value corresponding to key111


close container:
sudo docker-compose down
