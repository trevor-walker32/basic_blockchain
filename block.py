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
            self.set_hashstr(previous_block)
            self.set_hashval()
        elif genesis_block:
            self.set_hashstr()
            self.set_hashval()
        else:
            print("Error: did not generate a new block.")
            


    def get_timestamp(self):
        return self.timestamp

    def get_data(self):
        return self.data

    def get_hashval(self):
        return self.hash_val

    def get_hashstr(self):
        return self.hash_str
    
    def set_timestamp(self):
        self.timestamp = time.time()

    def set_data(self, data):
        if data:
            self.data = data
        else:
            self.data = "new data block"

    def set_hashstr(self, prevblock=None):
        try:
            if prevblock:
                assert isinstance(prevblock, Block)
                extra = prevblock.get_hashval()
            else: 
                extra = random.randint(0, 2**31)

            hash_data = str(self.get_data())
            hash_time = str(self.get_timestamp())
            hash_xtra = str(extra)

            self.hash_str = str(hash_data + hash_time + hash_xtra)
        except:
            print("Error: could not generate hash value for new block")
            
    def set_hashval(self):
        bhash_str = str(self.get_hashstr).encode('utf-8')
        self.hash_val = hashlib.sha256(bhash_str).hexdigest()

        


if __name__ == "__main__":

    firstblock = Block(genesis_block=True)
    secondblock = Block(previous_block=firstblock, genesis_block=False)
    thirdblock = Block(previous_block=secondblock, genesis_block=False)
    fourthblock = Block(previous_block=thirdblock, genesis_block=False)

    # print(firstblock.hash_val)
    # print(secondblock.hash_val)
    # print(thirdblock.hash_val)
    # print(fourthblock.hash_val)

    # print(firstblock.data)
    # print(secondblock.data)
    # print(thirdblock.data)
    # print(fourthblock.data)

    # print(firstblock.timestamp)
    # print(secondblock.timestamp)
    # print(thirdblock.timestamp)
    # print(fourthblock.timestamp)

    # print(firstblock.hash_str)
    # print(secondblock.hash_str)
    # print(thirdblock.hash_str)
    # print(fourthblock.hash_str)
