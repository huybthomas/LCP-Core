from system_configurator import SystemConfigurator
from logger import Logger
import time


class Core(object):
    __version = "0.1"

    def __init__(self):
        self.__logger_setup = Logger(to_terminal=True)
        self.__logger = self.__logger_setup.get_logger('Core')

        self.__logger.info("LCP Core - Version " + self.__version)
        self.__logger.info("Initialising system...")
        self.__SystemConfig = SystemConfigurator()
        self.__SystemConfig.load_config("..\\..\\..\\resources\\config.ini")

        print(">> Loading character configuration...")
        # lcp character configuration
        time.sleep(1)
        print(">> Start module loader...")
        self.__MLoader = ModuleLoader(self.__SystemConfig.get_module_config('ModuleLoader'))
        self.__MLoader.load_modules(self.__SystemConfig)

    def start(self):
        print(">> Booting core...")

        print(">> Booting modules...")
        self.__MLoader.start_modules()

        time.sleep(1)

        print(">> System ready")

        while 1:
            time.sleep(1)


if __name__ == "__main__":
    Core = Core()
    Core.start()
