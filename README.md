# Steps to setup the code

1. Create virtualenv and install dependencies 
```
pip install -r requirements.txt 
```

2. Run server using:
```
python manage.py runserver
```

3. Run celery server to perform async job
```
celery -A EmailApp worker --loglevel info
```

4. Run test case
```
python manage.py test
```