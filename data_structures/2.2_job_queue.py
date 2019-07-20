# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
FinishedJob = namedtuple("FinishedJob", ["worker", "finished_at"])

def parent(i):
    return (i - 1) // 2

def leftChild(i):
    return i*2 + 1

def rightChild(i):
    return i*2 + 2 
    
def siftUp(queue, i):
    while i > 0 and (queue[parent(i)].finished_at > queue[i].finished_at or \
                    (queue[parent(i)].finished_at == queue[i].finished_at and \
                     queue[parent(i)].worker > queue[i].worker)):
        queue[parent(i)], queue[i] = queue[i], queue[parent(i)]
        i = parent(i)
    
def siftDown(queue, i):
    minIndex = i
    l = leftChild(i)
    r = rightChild(i)
    if l < len(queue):
        if queue[l].finished_at < queue[minIndex].finished_at:
            minIndex = l
        elif queue[l].finished_at == queue[minIndex].finished_at and \
                    queue[l].worker < queue[minIndex].worker:
            minIndex = l
            
    if r < len(queue):    
        if queue[r].finished_at < queue[minIndex].finished_at:
            minIndex = r
        elif queue[r].finished_at == queue[minIndex].finished_at and \
                    queue[r].worker < queue[minIndex].worker:
            minIndex = r      
    
    if i != minIndex:
        queue[i], queue[minIndex] = queue[minIndex], queue[i]
        siftDown(queue, minIndex)

        
def insert(queue, p):
    queue.append(p)
    siftUp(queue, len(queue)-1)
    
def extractMin(queue):
    result = queue[0]
    queue[0] = queue[-1]
    queue.pop()
    siftDown(queue, 0)
    return result
    
def assign_jobs(n_workers, jobs):
    worker_queue = [FinishedJob(w, 0) for w in range(n_workers)]
    
    result = []
    
    for job in jobs:
        w = extractMin(worker_queue)
        result.append(AssignedJob(w.worker, w.finished_at))
        insert(worker_queue, FinishedJob(w.worker, w.finished_at+job))
        
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
