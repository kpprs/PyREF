class BusinessRuleException(Exception):
    """
    Custom exception to represent business rule violations.
    This does not indicate an error, but signals that the transaction
    should be set aside or handled differently.
    """
    def __init__(self, message, transaction_id=None):
        super().__init__(message)
        self.transaction_id = transaction_id