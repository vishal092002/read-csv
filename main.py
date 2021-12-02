
import logging

infoLogger = logging.getLogger()
infoHandler = logging.FileHandler('./results/calculator.log')
infoLogger.setLevel(logging.INFO)
infoLogger.addHandler(infoHandler)
infoLogger.info('Our First Log Message')

errorLogger = logging.getLogger()
errorHandler = logging.FileHandler('./results/error.log')
errorLogger.setLevel(logging.ERROR)
errorLogger.addHandler(errorHandler)
errorLogger.error('Our First erorr Message')