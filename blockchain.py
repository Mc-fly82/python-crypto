""" Blockchain lib """


blockchain = []


def get_last_blockchain_value():
    """ Get the last element in the blockchain"""
    return blockchain[-1] if len(blockchain) > 0 else None


def get_user_input(msg):
    """ Get a user input """
    output = input(msg+': \n')
    return output


def get_user_input_raw(msg):
    """ Get a user input raw apply no format to the message outputted """
    return input(msg)


def add_node_to_blockchain(transaction_amount, last_transaction):
    """ Add a Item to the blockchain 
    last_transaction: get the last blockchain node 
    transaction_amount: the given transaction amount
    """
    blockchain.append([last_transaction, transaction_amount])


def grouped_transaction(given_blockchain):
    """ Groupe transaction handler"""
    while True:
        user_operation_help = """
            Please choose
            1: Add a new transaction value
            2: Output the blockchain blocs
            q: To Quit
        """
        user_choice = get_user_input_raw(user_operation_help)
        choice_list = [str(item+1) for item in range(2)]
        choice_list.append('q')

        # choice 1
        if user_wants_to_add_a_new_transaction(user_choice):
            tx_amount = float(get_user_input('Your transaction please: '))
            add_node_to_blockchain(tx_amount, get_last_blockchain_value())
        # choice 2
        elif user_wants_to_output_the_blockchain(user_choice):
            output_blockchain(given_blockchain)
        # choice not handled
        elif user_choice not in choice_list:
            print('Input invalid, please choose a listed choice')
        else:
            # choice 3
            break


def user_wants_to_output_the_blockchain(user_choice):
    """ Check for a output blockchain operation """
    return str(user_choice) == '2'


def user_wants_to_add_a_new_transaction(user_choice):
    """ Check for a new transaction operation """
    return str(user_choice) == '1'


def output_blockchain(given_blockchain):
    """ Output the block chain """
    for block in given_blockchain:
        print('Outputting block')
        print(block)

if __name__ == "__main__":
    grouped_transaction(blockchain)
    print('God Bye!')
