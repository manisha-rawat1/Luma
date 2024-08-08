import pytest
import logging


@pytest.mark.usefixtures("setup")
class Baseclass:
    @staticmethod
    def logger():
        logging.basicConfig(filename=r"C:\Users\mrawat\PycharmProjects\Luma\logs\luma_site.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%y-%m-%d %H:%M:%S", force=True)
        logger = logging.getLogger(__name__)
        return logger
