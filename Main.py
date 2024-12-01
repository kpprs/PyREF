# import utility modules
import os
import pyodbc
import time
import pandas as pd
from datetime import datetime

# import exception class BRE from framework modules
# import core functions from framework modules
from Framework.ClassBRE import BusinessRuleException
from Framework.Logger import logger
from Framework.Initialization import Initialization
from Framework.GetTransactionData import GetTransactionItem
from Framework.Proces import Proces
from Framework.SetTransactionStatus import TransactionStatus
from Framework.End import End

# define the main function
def Main():
    """
    The Main function containing the core logic of the PyREF.

    It contains five central functions:
        _Initialization_:     Initializes the project config dictionary and gets any necessary third party software ready
        _GetTransactionItem_: Retrieves transaction data and each transaction item to be processed
        _Proces_:             Processes each transaction item according to its logic
        _TransactionStatus_:  Sets the status of each processed transaction item according to its result (succes or exception)
        _End_:                Ends the process with any relevant actions such as closing DB connections or writing data to a file
        
    """

    print('Starting process...')
    log = logger()
    log.info(f'User: {os.getlogin()}, procesID: {os.getpid()}')

    # declare main variables
    dictConfig: dict = {}
    intTransactionNumber: int = 0
    intMaxConsecutiveExceptions: int = 0
    boolInit: bool = False
    TransactionItem: object = None
    TransactionData: object = None
    SystemException: Exception = None
    BRException: BusinessRuleException = None

    # run while no errors have occurred
    while True:

        # if init has not run, run it
        # if init fails, go to End and break main loop
        if boolInit == False:
            try:
                dictConfig = Initialization(config=dictConfig, logger=log)
                boolInit = True
            
            except Exception as E:
                SystemException = E
                
                print('Ending process due to initialization error')
                log.critical(f'Ending process due an error during initialization: {SystemException}')
                
                End(config=dictConfig, argTD=TransactionData, argException=SystemException, logger=log)
                break

        # get the next transaction item to be processed
        # if getting the next items results in an error, go to End and break main loop
        # if there are no more items to proces, go to End and break main loop
        try:
            TransactionData, TransactionItem = GetTransactionItem(logger=log, config=dictConfig, argTI=TransactionItem, argTD=TransactionData, argTN=intTransactionNumber)
            if TransactionItem == None:
                print('Ending process due to no more transaction items')
                log.info('Process finished due to no more transaction items')
                
                End(config=dictConfig, argTD=TransactionData, logger=log)
                break

        except Exception as E:
            SystemException = E
            
            print('Error while retrieving the next transaction item; ending process')
            log.critical(f'Ending process due to failure to retrieve transaction item or data: {SystemException}')
            
            End(config=dictConfig, argTD=TransactionData, argException=SystemException, logger=log)
            break

        # proces each transaction item
        # if no error is raised, run TransactionStatus for that item and continue to the next
        # if an exception (sys or BRE) is raised, it will be caught and handled by TransactionStatus
        # any error is then set to None, and the main loop continues
        # if the maximum allowed number of consecutive exceptions is reached, go to End and break main loop 
        try:
            TransactionItem = Proces(config=dictConfig, argTN=intTransactionNumber, argTI=TransactionItem, logger=log)
            intTransactionNumber, TransactionData = TransactionStatus(config=dictConfig, argTI=TransactionItem, argTD=TransactionData, argTN=intTransactionNumber, logger=log)
        
        except BusinessRuleException as BRE:
            BRException = BRE
            
            print('Business Rule Exception encountered during processing of transaction item')
            log.info(f'Business Rule Exception encountered during processing of transaction item: {TransactionItem}, {BRException}')
            
            intTransactionNumber, TransactionData = TransactionStatus(config=dictConfig, argTI=TransactionItem, argTD=TransactionData, argTN=intTransactionNumber, logger=log, argBRE=BRException)
            BRException = None

        except Exception as E:
            SystemException = E
            intMaxConsecutiveExceptions = intMaxConsecutiveExceptions +1
            
            print('Error encountered during processing of transaction item')
            log.error(f'Exception encountered during processing of transaction item {TransactionItem}: {SystemException}; consecutive exceptions: {intMaxConsecutiveExceptions}')
            
            intTransactionNumber, TransactionData = TransactionStatus(config=dictConfig, argTN=intTransactionNumber, argTI=TransactionItem, argTD=TransactionData, argException=SystemException, logger=log)
            SystemException = None
            
            if intMaxConsecutiveExceptions == dictConfig['Max consecutive exceptions']:
                print('Ending process due to maximum consecutive exceptions')
                log.critical('Ending process due maximum consecutive exceptions')
                
                End(config=dictConfig, argTD=TransactionData, logger=log)
                break

# run the main function as defined above
if __name__ == '__main__':
    Main()