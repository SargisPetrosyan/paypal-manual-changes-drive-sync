from app.core.config import Database
from app.core.logging import setup_logger
from app.google_drive.drive_sync_worker import HourlyWorkflowRunner
import logging 

setup_logger()

logger: logging.Logger = logging.getLogger(name=__name__)

if __name__ == '__main__':
    logger.info("run worker")
    workflow_runner = HourlyWorkflowRunner(database=Database())
    workflow_runner.run()