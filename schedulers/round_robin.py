from collections import deque
from schedulers import base
from defines import COMPLETE
from defines import INCOMPLETE

"""
#==================================================
Round Robin Scheduler

The idea behind this scheduler is to assign a fixed
time slot for each process, called a quantum. The 
processes are executed in a cyclic way. Once a 
process is executed for a given time period, it's 
preempted and the next process executes for its 
time period. Context switching is used to save the
states of preempted processes.
#==================================================
"""

class RR(base.BaseScheduler):
    #==============================================
    #Intialize the run queue for RR
    #Params:
    #   processQ = Deque of processes to run
    #   timerInterrupt = Allows scheduler to check
    #                    on running process and to
    #                    make decisions
    #Return:
    #   None
    #==============================================
    def __init__(self, processQ, timerInterrupt):
        super().__init__(processQ, timerInterrupt)
        self.readyList = deque([])

    #==============================================
    #Checks to see if the queue is empty
    #Params:
    #   None
    #Return:
    #   Boolean indiciating if queue is empty or
    #   not
    #==============================================
    def empty(self):
        return len(self.readyList) == 0

    #==============================================
    #Add a process to the end of the run queue
    #Param:
    #   1) process = the process to be added
    #Return:
    #   None
    #==============================================
    def addProcess(self, process):
        self.readyList.append(process)
    
    #==============================================
    #Get the next process on the queue
    #Params:
    #   None
    #Return:
    #   Next process on the queue
    #   None if no process in queue
    #==============================================
    def removeProcess(self):
        try:
            return self.readyList.popleft()
        except IndexError:
            return None
    
    #==============================================
    #Get the next process for the scheduler to run.
    #This implements the scheduler heuristics
    #Params:
    #   curProc = Current process that's running on
    #             scheduler
    #Return:
    #   Next process in the queue via call to 
    #   removeProcess()
    #==============================================
    def getNext(self, curProc):
        if curProc is not None and curProc.get_status() == INCOMPLETE:
            self.addProcess(curProc)
        elif curProc is not None and curProc.get_status() == COMPLETE:
            curProc = None
        return self.removeProcess()
