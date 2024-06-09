from multiprocessing import Pool
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_lists(numbers):
    try:
        return sum(numbers)
    except Exception as e:
        logger.error(f"Error adding list {numbers}: {e}")
        return None

def addition_controller(lists):
    with Pool(processes=len(lists)) as pool:
        results = pool.map(add_lists, lists)
    return results
