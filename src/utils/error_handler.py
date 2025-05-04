import logging

logging.basicConfig(level=logging.INFO)

def handle_error(error, message="An error occurred:"):
    logging.error(f"{message} {error}")
    # TODO: Implement error handling logic (e.g., retry, alert)
    return False