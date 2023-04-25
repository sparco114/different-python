# -*- coding: utf-8 -*-

import logging.config

log_confi = {
    "version": 1,
    "formatters": {
        "primes_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "main_formatter": {
            "format": "%(asctime)s - %(message)s"
        },
    },
    "handlers": {
        "primes_handler": {
            "class": "logging.FileHandler",
            "formatter": "primes_formatter",
            "filename": "primes.log",
            "encoding": "UTF-8",
        },
        "main_handler": {
            "class": "logging.FileHandler",
            "formatter": "primes_formatter",
            "filename": "main.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "primes": {
            "handlers": ["primes_handler"],
            "level": "DEBUG",
        },
        "master": {
            "handlers": ["main_handler"],
            "level": "INFO",
        },
    },
}

logging.config.dictConfig(log_confi)
