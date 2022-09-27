import time
from mp import Multiprocesser

class NumberProcessor(Multiprocesser):
    def run(self, num):
        time.sleep(3)
        return num