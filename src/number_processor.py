import time
import mp

class NumberProcessor(mp.Multiprocesser):
    def run(self, num):
        time.sleep(3)
        return num