# django-giom

reading data from giom in XML and store it to statsd and fluentd logger 

## requirement settings in django app:

 * GIOM_URL: giom url to gather data

## set up loggers
 * for fluentd or td-agent  use handler name fluend.giom
 * for django human readable logger handler use django.giom
    
### settings.py
```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'fluent': {
                'level': 'INFO',
                'db': '[your DB name]',
                'table': '[your table name]',
                'class': 'tdlog.logger.TreasureDataHandler'
            }
        },
        'loggers': {
            'django.giom': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'fluend.giom': {
                'handlers': ['fluent'],
                'level': 'INFO',
                'propagate': True
            }
        },
    }
```

## setup CELERY BEAT scheduler (optional)
```python
    CELERYBEAT_SCHEDULE = {
        'refresh_giom_data': {
            'task': 'giom.tasks.refresh_giom_data',
            'schedule': timedelta(minutes=1)
        }
    }
```