import logging, logging.handlers
import sys
class debug_logger(object):
    def start_logger(self,name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        if not len(logger.handlers):
            fh = logging.handlers.RotatingFileHandler('log/pokerprogram.log', maxBytes=2000000, backupCount=0)
            fh.setLevel(logging.DEBUG)
            fh2 = logging.handlers.RotatingFileHandler('log/pokerprogram_info_only.log', maxBytes=2000000, backupCount=0)
            fh2.setLevel(logging.INFO)
            fh3 = logging.handlers.RotatingFileHandler('log/values.log', maxBytes=1000000, backupCount=10)
            fh3.setLevel(logging.CRITICAL)
            er = logging.handlers.RotatingFileHandler('log/errors.log', maxBytes=2000000, backupCount=2)
            er.setLevel(logging.WARNING)
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.WARNING)
            fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            fh2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            er.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            ch.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(fh)
            logger.addHandler(fh2)
            logger.addHandler(ch)
            logger.addHandler(er)
            logger.addHandler(fh3)
        return logger