logging_config = {
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
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'verbose'
        },
        'prod': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'uvicorn.error': {
            'propagate': False,
            'handlers': ['console'],
        },
        'trainer': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        }
    },
}