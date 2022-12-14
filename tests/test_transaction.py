import unittest
from transaction import Transaction
from tests.mock_utils import generate_single_transaction
from utils.helpers import isfloat


class TestTransaction(unittest.TestCase):
    def test_create_transaction_instance(self):
        givenPrimeTransaction = generate_single_transaction(
            sender="Marc", recipient="Bob", amount=10
        )
        instance = Transaction(givenPrimeTransaction)
        transactionOfInstance = instance.__dict__
        assert transactionOfInstance["sender"] == "Marc"
        assert transactionOfInstance["recipient"] == "Bob"
        assert transactionOfInstance["amount"] == 10
        assert isfloat(transactionOfInstance["created_at"])
