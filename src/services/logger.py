import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FelixApp")

def log_query(query: str, source: str):
    logger.info(f"Query from {source}: {query}")
