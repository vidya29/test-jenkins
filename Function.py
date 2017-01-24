import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_prime(number):
    logger.info("Return True if *number* is prime.")
    for element in range(2, number):
        if number % element == 0:
            return False

    return True

def print_next_prime(number):
    logger.info("Print the closest prime number larger than *number*.")
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)