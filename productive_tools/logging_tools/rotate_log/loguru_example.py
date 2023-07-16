from loguru import logger

logger.add("debug.log", level="INFO", rotation="1 week", retention="4 weeks")


def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()
