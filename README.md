# How to call cron with docker

requirements.txt not used in this example

script write time every minute all stay in docker container

you can access to date.txt in docker in root folder


## Usage ##

terminal:

git clone https://github.com/Ziga12341/docker-cronjob.git

cd docker-cronjob

docker build -t cronjob-datetime .

docker run -d cronjob-datetime

docker ps

    it will list all containers

    copy container id from image cronjob-datetime (something like 34681b275e96)

docker exec -it 34681b275e96 sh

    opens console inside your docker
    NOTE: you need to change container ID

cd root

cat date.txt 

    Now you see datetime when cron call python script like this:
    ~ # cat date.txt
    Time is: 2023-01-27 09:54:00.700564
    Time is: 2023-01-27 09:55:00.696705
    Time is: 2023-01-27 09:56:00.698455
    Time is: 2023-01-27 09:57:00.700820

exit
    
    to exit from docker container terminal