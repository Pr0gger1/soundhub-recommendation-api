import logging

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.DEBUG,
    filename="app.log"
)

logging.getLogger('kafka').setLevel(logging.WARNING)
logging.getLogger('kafka.client').setLevel(logging.WARNING)
logging.getLogger('kafka.conn').setLevel(logging.WARNING)
logging.getLogger('kafka.consumer').setLevel(logging.WARNING)
logging.getLogger('kafka.producer').setLevel(logging.WARNING)
logging.getLogger('kafka.fetcher').setLevel(logging.WARNING)
logging.getLogger('kafka.group').setLevel(logging.WARNING)
logging.getLogger('kafka.parser').setLevel(logging.WARNING)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
