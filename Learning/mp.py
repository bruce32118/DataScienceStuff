import multiprocessing
import os


def task(args):
    print("Running process", os.getpid(), "with args", args)
    return os.getpid(), args


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = pool.map(task, [1,2,3,4]*3)
    print(result)