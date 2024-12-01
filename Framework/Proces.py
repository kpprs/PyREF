# import regex for utility
# import os for utility
# import business rule exception
import re
import os
from Framework.ClassBRE import BusinessRuleException

def Proces(logger, config: dict, argTN: int, argTI: object):
    """
    The central function processing each new transaction item according to the logic relevant to the transaction data.

    It takes four positional arguments:
        argTI (object): the transaction item to be processed
        argTN (int): the index of the current transaction item
        config (dict): the project config dictionary
        logger (logger): the central project logger

    Return:
        Any relevant objects; returns transaction item by default
    """
    
    # include appropriate logic to handle project specific transactions
    
    print(f'Processing transaction number: {argTN +1}')
    logger.info(f'Processing transaction number: {argTN +1}')

    if argTI == 5:
        raise BusinessRuleException('Someone else takes care of this number')
    elif argTI == 13:
        raise Exception('Wrong number')