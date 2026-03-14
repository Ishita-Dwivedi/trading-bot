import logging
import os

def setup_logging():

    # create logs folder if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = os.path.join("logs", "bot.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a"
    )

    logging.info("Logging initialized")