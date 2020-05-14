"""
Chain class for building blockchains in python. Inherits the Block class.
"""

import block
import copy


class Chain:

    def __init__(self):

        self.blocks = list()
        # self.identifier

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False


    def get_genesis_block(self):
        assert (len(self.blocks) >= 0)
        return self.blocks[0]

    def get_most_recent(self):
        assert (len(self.blocks) >= 0)
        return self.blocks[-1]

    def get_block_i(self, i:int):
        assert (len(self.blocks) >= 0)
        assert (i >= 0)
        assert (i < len(self.blocks))
        return self.blocks[i]

    def get_chainsize(self):
        return len(self.blocks)


    def add_block(self, data):

        if (len(self.blocks) == 0):
            new_block = block.Block(data, genesis_block=True)
        else:
            most_recent_block = self.get_most_recent()
            new_block = block.Block(data, previous_block=most_recent_block)
        self.blocks.append(new_block)

    
    def fork_chain(self):
        return copy.deepcopy(self)

    
    def verify(self): 
        for i in range(1,len(self.blocks)):

            current_block = self.get_block_i(i)
            prev_block = self.get_block_i(i-1)
            current_data = current_block.data
            current_timestamp = current_block.timestamp
            prev_hashval = prev_block.get_hashval()

            if current_block.index != i:
                print(f'Wrong block index at block {i}.')
                return False
            if prev_block != current_block.previous_block:
                print(f'Conflicting ordering of blocks {i} and {i-1}.')
                return False
            if self.blocks[i-1].hash_val != prev_hashval:
                print(f'Conflicting hashes at block {i}.')
                return False
            if current_block.hash_val != block.hash_function(current_data, current_timestamp, prev_hashval):
                print(self.blocks[i].get_hashstr())
                print(self.blocks[i].hash_function())
                print(f'Could not recreate hash at block {i}.')
                return False
            if prev_block.timestamp >= current_block.timestamp:
                print(f'Backdating detected at block {i}.')
                return False
        print("this chain appears to be correct")
        return True



if __name__ == "__main__":

    new_chain = Chain()

    for i in range(5):
        data = "block number "+str(i)
        new_chain.add_block(data)
    
    fork = new_chain.fork_chain()

    fork.verify()
    
    new_chain.verify()