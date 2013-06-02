ps aux | grep python | grep port | awk '{print $2}' | xargs kill; python ./manage.py runfcgi host=127.0.0.1 port=8080
