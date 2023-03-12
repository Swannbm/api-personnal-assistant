import logging
import uvicorn

from .config import PORT

logger = logging.getLogger(__name__)


def serve():
    """Run function for Scalingo, see `Procfile`"""
    logger.info(f"Running uvicorn on {PORT}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, workers=1)


if __name__ == '__main__':
    serve()
