podexporter.py отправляет запрос на 'https://10.73.1.115:8443/api/v1/pods'

docker build -t pod .
docker run -it --name=numpod -p 8088:8088 pod (для проверки)

в Pod указываем этот Image: pod  и что собирается только из локального репо.
Запускаем Pod и его Service  видим http://10.73.1.115:8088/  запустился экспортер и его таргет появился в прометеус


