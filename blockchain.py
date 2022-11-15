""" Blockchain lib """
import re

genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}

owner = "Marc"
participants = set([owner])
blockchain = [genesis_block]
open_transaction = []
MINING_TRANSACTION = 5

def grouped_transaction():
    """ Groupe transaction handler """
    global participants
    global open_transaction
    global blockchain

    while True:
        user_operation_help = """
            Please choose
            1: Add a new transaction value
            2: Output the blockchain blocs
            3: Mind transaction
            4: List participants
            5: List open transactions
            6: Output user balance
            q: To Quit
        """
        user_choice, choice_list = get_user_choice(user_operation_help)

        if user_wants_to_quit(user_choice):
            break
        elif user_wants_to_add_a_new_transaction(user_choice):
            transaction_data = get_user_transaction()
            amount, recipient = transaction_data
            add_transaction(recipient, amount=amount)
        elif user_wants_to_output_the_blockchain(user_choice):
            output_blockchain(blockchain)
        elif user_wants_to_mind_new_block(user_choice):
            mine_block()
        elif user_wants_to_output_open_transaction(user_choice):
            output_open_transactions(open_transaction)
        elif user_wants_to_output_participants(user_choice):
            output_participant(participants)
        elif user_wants_to_output_balance(user_choice):
            output_user_balance(owner)
        # choice not handled
        elif user_choice not in choice_list:
            print('Input invalid, please choose a listed choice')
        else:
            # choice 3
            break

def verify_chain():
    """ Verify the blockchain integrity """
    block_index = 0
    is_valid = True
    for current_block in blockchain:
        prev_block = blockchain[block_index - 1]["previous_hash"]
        if current_block != prev_block:
            is_valid = False
            break
    return is_valid if current_block["previous_hash"] == {} else True

def reset_blockchain():
    """ Wipe the blockchain """
    global blockchain
    blockchain = []

def get_last_blockchain_value():
    """ Get the last element in the blockchain """
    global genesis_block
    global blockchain
    return blockchain[-1] if len(blockchain) > 0 else genesis_block

def get_user_input(msg):
    """ Get a user input """
    output = input(msg+': \n')
    return output

def get_user_input_raw(msg):
    """ Get a user input raw apply no format to the message outputted """
    return input(msg)

# TODO: Marc Flavius - fix sender
def add_transaction(recipient, sender="Marc", amount=1.0):
    """ Add a Item to the blockchain 
    sender: the sender of the coins. 
    recipient: the recipient of the coins.
    amount: the given transaction amount
    """
    global open_transaction
    transaction = {"sender": sender, "recipient": recipient, "amount": amount, }
    open_transaction.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    """ Add all open transaction to a block and wipe the open transaction array"""
    global blockchain
    global open_transaction
    reward_transaction =  {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_TRANSACTION, 
    }
    open_transaction.append(reward_transaction)
    hashed_block = hash_block()
    new_block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": open_transaction,
    }
    blockchain.append(new_block)
    verify_chain()
    open_transaction = []

def hash_block():
    last_block = get_last_blockchain_value()
    hashed_block = ""
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)
    return hashed_block

def get_user_transaction():
    """ Get user input transaction"""
    recipient = (""+get_user_input('Enter the recipient of the transaction: ')).capitalize()
    tx_amount = get_numeric_input('Your transaction please: ')
    return tx_amount, recipient

def get_numeric_input(input):
    tx_amount=input
    match = len(re.findall("[0-9]+$",tx_amount))
    if match != 1:
        print('Please enter a numeric amount\n')
        tx_amount = get_numeric_input(get_user_input(input))
    return int(tx_amount)

def get_user_choice(user_operation_help):
    """ Get user choice """
    user_choice = get_user_input_raw(user_operation_help)
    choice_list = [str(item+1) for item in range(2)]
    choice_list.append('q')
    return user_choice, choice_list,

def user_wants_to_quit(user_choice):
    return user_choice == "q"

def user_wants_to_add_a_new_transaction(user_choice):
    """ Check for a new transaction operation """
    return str(user_choice) == '1'

def user_wants_to_output_the_blockchain(user_choice):
    """ Check for a output blockchain operation """
    return str(user_choice) == '2'

def user_wants_to_mind_new_block(user_choice):
    return str(user_choice) == '3'

def user_wants_to_output_participants(user_choice):
    return str(user_choice) == '4'

def user_wants_to_output_open_transaction(user_choice):
    return str(user_choice) == '5'

def user_wants_to_output_balance(user_choice):
    return str(user_choice) == '6'

def output_blockchain(given_blockchain):
    """ Output the block chain """
    for block in given_blockchain:
        print('Outputting block...')
        print(block)

def output_participant(participants):
    print(participants)
    return participants 

def output_open_transactions(open_transactions):
    print(open_transactions)
    return open_transaction

def get_user_balance(user_id):
    global blockchain

    last_block = get_last_blockchain_value()
    transactions = last_block['transactions']
    
    received = sum([block['amount'] for block in transactions if block['recipient'] == user_id ])
    sent = sum([block['amount'] for block in transactions if block['sender'] == user_id ])

    return received - sent

def output_user_balance(user_id):
    balance=get_user_balance(user_id)
    print(balance)
    return balance

if __name__ == "__main__":
    grouped_transaction()
    print('God Bye!')
