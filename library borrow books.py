import hashlib
import datetime

class Transaction:
    def __init__(self, borrower, book_id):
        self.borrower = borrower
        self.book_id = book_id
        self.timestamp = str(datetime.datetime.now())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        hash_str = self.borrower + self.book_id + self.timestamp
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Block:
    def __init__(self, transactions, previous_block_hash):
        self.transactions = transactions
        self.previous_block_hash = previous_block_hash
        self.timestamp = str(datetime.datetime.now())
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.transactions) + self.previous_block_hash + self.timestamp + str(self.nonce)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block([], '0')

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_block_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_block_hash != previous_block.hash:
                return False
        return True

# Example usage
library_blockchain = Blockchain(2)  # Set the difficulty to 2

# Create some transactions for borrowing and returning books
transaction1 = Transaction('Minsu', 'The Little Prince')
transaction2 = Transaction('Jihyun', 'Pride and Prejudice')
transaction3 = Transaction('Sungwoo', 'The Hobbit')
transaction4 = Transaction('Minsu', 'The Little Prince')

# Create some blocks and add the transactions to the blockchain
block1 = Block([transaction1, transaction2], '0')
library_blockchain.add_block(block1)

block2 = Block([transaction3, transaction4], library_blockchain.get_last_block().hash)
library_blockchain.add_block(block2)

# Check if the blockchain is valid
print("Is the blockchain valid?", library_blockchain.is_valid_chain())
