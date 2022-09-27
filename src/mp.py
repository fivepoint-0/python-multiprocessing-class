from multiprocessing import Pool, cpu_count

class Multiprocesser:
    def __init__(self, array_of_args, processes: int = cpu_count()):
        self.args = array_of_args
        self.processes = processes

    def run(self, arg):
        return arg

    def execute(self):
        with Pool(processes=4) as pool:
            results = pool.starmap(self.run, [tuple(arg_set) for arg_set in self.args])
        return results