
import queue 
import block
import time

class Miner:

    def __init__(self, miner_id):

        self.queue = queue.Queue()
        self.miner_id = miner_id
        self.found_hash = None


    def simulate_proof_of_work(self, level_of_difficulty:int, nonce_method:bool = False, timestamp_method:bool = False):
        
        dummy_block = block.Block("data", previous_block=None, genesis_block=True)
        nonce = 0
        timestamp = time.time()
        hashed_value = block.hash_function("data", timestamp, dummy_block.hash_val, nonce)
        difficult_string = "0" * level_of_difficulty

        if nonce_method:
            while(hashed_value[:level_of_difficulty] != difficult_string):
                nonce += 1
                hashed_value = block.hash_function("data", timestamp, dummy_block.hash_val, nonce)
                self.found_hash = hashed_value

        elif timestamp_method:
            while(hashed_value[:level_of_difficulty] != difficult_string):
                timestamp = time.time()
                hashed_value = block.hash_function("data", timestamp, dummy_block.hash_val, nonce)
                self.found_hash = hashed_value

        else:
            print("must specify method to use to simulate proof of work")
            print("ex. nonce_method=True or timestamp_method=True")




if __name__ == "__main__":

    miner = Miner(1)

    miner.simulate_proof_of_work(5, timestamp_method=True)

    print(miner.found_hash)