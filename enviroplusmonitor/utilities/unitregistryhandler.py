import logging

import utilities.configurationhandler as configurationhandler
import pint

module_logger = logging.getLogger(
    configurationhandler.config["logging"]["MODULE_LOGGER"]
)


ureg = None


def configure():
    global ureg
    # import unit registry and definitions
    ureg = pint.UnitRegistry()
    module_logger.info("./resources/default_en.txt")
    ureg.load_definitions("./resources/default_en.txt")
