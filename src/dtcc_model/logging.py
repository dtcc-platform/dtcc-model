# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import logging
format = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"
logging.basicConfig(format=format, level='DEBUG')
logger = logging.getLogger('dtcc_model')

debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
