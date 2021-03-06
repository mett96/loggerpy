if __name__ == '__main__':
    from loggerpy import Logger, Level

    logger = Logger()
    logger.name = "First logger"
    logger.folder = "/Users/jarvis/Documents/workspace/Python/loggerpy/test"
    logger.print_level = Level.DEBUG
    logger.save_level = Level.DEBUG

    logger.debug('Debug test')
    logger.info('Info test')
    logger.warning('Warning test')
    logger.error('Error test')
    logger.critical('Critical test')
