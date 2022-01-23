import logging

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('[%(asctime)s]:[%(levelname)s]:: %(message)s', '%H:%M:%S'))
    logger.addHandler(handler)

def log_discord():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    return logger

def log_console():
    logger = logging.getLogger(__name__)
    return logger