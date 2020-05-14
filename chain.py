"""
Chain class for building blockchains in python. Inherits the Block class.
"""

import block
import copy


class Chain:

    def __init__(self):

        self.blocks = list()


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


if __name__ == "__main__":

    new_chain = Chain()

    for i in range(5):
        data = "block number "+str(i)
        new_chain.add_block(data)

    for i in range(5):
        block_i = new_chain.get_block_i(i)

        print(block_i.hash_val,'\n')

    fork = new_chain.fork_chain()

    fork.add_block("block number 5")

    print(fork.get_chainsize(), new_chain.get_chainsize())