from multiprocessing import Pool

class Multiprocesser:
    processes: int = 0
    args = None

    def __init__(self, array_of_args, processes: int = 4):
        self.args = array_of_args
        self.processes = processes

    def run(self, arg):
        return arg

    def execute(self):
        with Pool(processes=4) as pool:
            results = pool.starmap(self.run, [tuple(arg_set) for arg_set in self.args])
        return results