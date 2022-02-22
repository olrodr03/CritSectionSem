from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock

N = 8
def task(lock, common, tid):
    for i in range(100):
        lock.acquire()
        try:
            print(f'{tid}-{i}: Critical section', flush = True)
            v = common.value + 1
            print(f'{tid}-{i}: Inside critical section', flush = True)
            common.value = v
            print(f'{tid}-{i}: End of critical section', flush = True)
        finally:
            lock.release()
def main():
    lp = []
    common = Value('i', 0)
    lock = Lock()
    for tid in range(N):
        lp.append(Process(target=task, args=(lock, common, tid)))
    print(f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
        
    print(f"Valor final del contador {common.value}")
    print("fin")
    
if __name__ == "__main__":
    main()