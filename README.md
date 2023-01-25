# How to call cron with docker

requirements.txt not used in this example

script write time every minute all stay in docker container

you can access to date.txt in docker in root folder

in terminal:
docker build -t cronjob-datetime .
docker run -d cronjob-datetime
