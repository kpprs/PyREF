# import business rule exception
from Framework.ClassBRE import BusinessRuleException

def TransactionStatus(logger, argTN: int, argTI: object, argTD: object = None, argException: Exception = None, argBRE: BusinessRuleException = None, config: dict = None) -> tuple:
    """
    The function sets the status for each transaction according to its result:

        If no errors occurred during processing, the transaction was a succes and the transactio number is incremented.
        If any errors occurred during processing, the transaction failed, and the previous transaction is retried by not incrementing the transaction number.

    It takes three positional arguments and four optional arguments:
        (P) argTN (int): the transaction number to be incremented
        (P) argTI (object): the transaction item whose status needs to be updated
        (P) logger (logger): the central project logger
        (O) argTD (object): the transaction data bulk
        (O) argException (exception): any exception that might be relevant
        (O) argBRE (BusinessRuleException): any BRE that might have occurred during processing
        (O) config (dict): the project config dictionary

    Return:
        argTN (int): the updated transaction number
        argTD (object): the transaction data bulk
    """
    
    # include project specific logic to handle setting transaction status such as writing to a database or otherwise
    # set status for the transaction item according to result: success, BRE or exception
    if (argException == None and argBRE == None):
        Status = 'Success'
        print('Transaction succesful')
        logger.info(f'Transaction status: {Status}')
        
        # increment transaction number
        argTN = argTN +1
    elif argBRE:
        Status = 'Business Rule Exception'
        print('Transaction not completed due to Business Rule Exception')
        logger.info(f'Transaction status: {Status}, {argBRE}')
        
        # increment transaction number
        argTN = argTN +1
    else:
        Status = 'Error occurred during processing of transaction item'
        print('Transaction failed; retrying...')
        logger.warning(f'Transaction failed: {argException}')
        logger.info('Retrying transaction...')

    return argTN, argTD