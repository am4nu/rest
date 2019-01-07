# RestAPI
Hello Rest API , built with flask, docker, sqlalchemy


Make sure you are on ubuntu >=16.04

on the terminal run:
$ git clone -b nopost https://github.com/mdamanuddin/rest && cd rest

After that run:

$ sh install.sh


It will ask for the name of the container just input any name you want




now to test the enpoints open any browser type the following url to test the endpoints:

This is implemented according to use case given

http://localhost:5000/hello/"string"

To see the database  enter the url in the browser:
http://localhost:5000/db

if you don't have browser you can use wget from commandline

$ wget http://localhost:5000/hello/"string"

$ wget http://localhost:5000/db






