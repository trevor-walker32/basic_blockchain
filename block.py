"""
Block class for building basic blockchains in python. 
"""

import time 
import hashlib
import random

class Block:

    def __init__(self, 
                data,
                previous_block = None, 
                genesis_block = False
                ):
                
        assert (data is not None)

        self.set_timestamp()
        self.set_data(data)
        if previous_block:
            assert isinstance(previous_block, Block)
            self.set_hashval(previous_block)
            self.set_index(previous_block.index + 1)
            self.previous_block = previous_block
            self.genesis_block = False
        elif genesis_block:
            self.set_hashval(None)
            self.set_index(0)
            self.previous_block = None
            self.genesis_block = True
        else:
            print("Error: did not generate a new block.")
            


    def get_timestamp(self):
        return self.timestamp

    def get_data(self):
        return self.data

    def get_hashval(self):
        return self.hash_val

    def get_index(self):
        return self.index

    def get_hashstr(self):
        return self.hash_str

    def set_timestamp(self):
        self.timestamp = time.time()

    def set_index(self, index):
        self.index = index

    def set_data(self, data):
        if data:
            self.data = data
        else:
            self.data = "new data block"

            
    def set_hashval(self, prevblock):

        if prevblock:
            assert isinstance(prevblock, Block)
            extra = prevblock.get_hashval()
        else: 
            extra = random.randint(0, 2**31)

        hash_data = str(self.get_data())
        hash_time = str(self.get_timestamp())
        hash_xtra = str(extra)

        self.hash_val = hash_function(hash_data, hash_time, hash_xtra)

def hash_function(data, time, xtra):
    bhash_str = (str(data) + str(time) + str(xtra)).encode('utf-8')
    return hashlib.sha256(bhash_str).hexdigest()

if __name__ == "__main__":

    firstblock = Block(genesis_block=True)
    secondblock = Block(previous_block=firstblock)
    thirdblock = Block(previous_block=secondblock)
    fourthblock = Block(previous_block=thirdblock)

