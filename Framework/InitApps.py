def InitApps(config: dict = None, logger = None):
    """
    The function initializes any necessary third party software,
    such as opening database connections, checking API-statuses or opening web sites.

    Takes two optional arguments:
        config (dict): a project dictionary defined in Initialization 
        log (logger): a logger defined in Main

    Return:
        Any objects necessary to proces transaction items.
    """
    
    # include project specific logic to initialize third party software 

    logger.info('Opening applications')