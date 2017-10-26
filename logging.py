import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# to disable logging, remove the comment that precedes the code in the next line
#logging.disable(logging.CRITICAL)
logging.debug('Starting the program')


def bug(fly):
    logging.debug('fly = {}'.format(fly))
    fly = 'fly'
    logging.debug('fly = {}'.format(fly))
    return fly


bug('vlieg')
print('Hello')

logging.debug('The program is finished')

