from loguru import logger
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
logger.remove(0)
handler = logger.add(sys.stdout,  level="TRACE", serialize=True)
new_level = logger.level("NOTIFICATION", no=26, color="<yellow>", icon="🐍")
#logger.log("NOTIFICATION", "Here we go!")
#logger.info("test")
#logger.bind(experiment_id=123).trace("Hello sadedegel")
#logger.bind(experiment_id=123).log("NOTIFICATION", "Here we go!")
def test():
    logger.log("NOTIFICATION","test")
    logger.bind(experiment_id=123).trace("Hello sadedegel")
    logger.debug("Hello sadedegel")
    logger.info("Hello sadedegel")
    logger.warning("Hello sadedegel")
    logger.error("Hello sadedegel")
    logger.critical("Hello sadedegel")

test()