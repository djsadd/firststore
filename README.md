<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154439.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154516.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154530.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154536.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154615.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-22%20154711.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-26%20234014.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-26%20234024.png">
<img src="https://github.com/djsadd/firststore/blob/main/store/static/vendor/img/Снимок%20экрана%202023-09-26%20234035.png">


# First step: install env and install requirements.txt 
  > - ```python3 -m venv {myenvname}```
  > - ```source {myenvname}/Scripts/activate```
  > - ```pip install requierements.txt```

# Second step install redis
1. https://redis.io/docs/getting-started/ - documentation for install redis.
2. run redis

# Third step run celery
1. in venv write command: celery -A store worker -l INFO

# Fourth step install stripe
1. <p><a href="https://stripe.com/docs/stripe-cli">Download stripe </a> in your os and and move 'stripe' file to root project on one level with 'manage.py'</p>
2. In terminal write command: "stripe listen --forward-to 127.0.0.1:8000/webhook/stripe/"
