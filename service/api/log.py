import logging
import logging.config

logging.config.fileConfig(fname='api/log.conf', disable_existing_loggers=False)
logger = logging.getLogger("root")
