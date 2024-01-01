# OpenSky Report Dash App

## Development Guide

Activate virtual environment, i.e. virtualenv:
```
source myvenv/bin/activate
```

To run the app:
```
python app/app.py 
```

Via gunicorn:
```
gunicorn -c app.server.gunicorn app.app:server
```

### Author
By Kenny William Nyallau