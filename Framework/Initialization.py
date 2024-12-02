# import json
# import os 
# import InitApps from Framework
import json
import os
from Framework.InitApps import InitApps

def Initialization(config: dict = None, logger=None):
    """
    The function reads the config file in json format and returns a dictionary.

    The function runs once upon start-up and each time an exception occurs during processing of a transaction item.

    Takes two optional arguments:
        config (dict): a dictionary defined in Main
        log (logger): a logger defined in Main

    Return:
        config (dict): a config dictionary containing project specific data such as file paths and urls
    """

    # include additional project specific initialization logic

    print('Getting things ready...')
    # read the json config file and get config dictionary
    with open('Data/Config.json', 'r') as configFile: 
        config = json.load(configFile)

    logger.info('Config ready')
    
    # init any applications or other necessary third party software
    # include any returned object in return in this function
    InitApps(config=config, logger=logger)
    
    return config