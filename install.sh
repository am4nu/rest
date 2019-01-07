echo "enter name of docker image that you want"
read name_image
sudo apt-get install docker.io
sudo docker build -t $name_image .
sudo docker run -it -p 80:5000 $name_image
