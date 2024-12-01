def GetTransactionItem(argTN: int, argTI: object, argTD: object, logger = None, config: dict = None) -> tuple:
    """
    The function retrieves the transaction data and each transaction item to be processed. 

    It takes three positional arguments and two optional arguments:
        (P) argTN (int): the index of the next transaction to be processed, defined in main
        (P) argTI (object): the next transaction item to be processed, defined in main
        (P) argTD (object): the transaction data bulk containing the data to be processed, defined in main
        (O) config (dict): the project config dictionary, defined in main
        (O) logger (logger): the central project logger, defined in main

    Return:
        argTD (object): the transaction data bulk
        argTI (object): the next transaction item
    """
    
    logger.info('Getting the next transaction item')
    
    # if transaction data is none, retrieve it
    # substitute with appropriate logic to retrieve project specific transaction data
    if argTD == None:
        argTD = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    # get the next transaction item
    # substitute with appropriate logic to retrieve project specific transaction item
    if argTN < len(argTD):
        argTI = argTD[argTN]
    else:
        argTI = None
 
    return argTD, argTI