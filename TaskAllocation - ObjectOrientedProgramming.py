
class Task(object):
    
    def __init__(self,TaskType,TaskID,TaskPriority):
        self.TaskID = TaskID
        self.TaskType = TaskType
        self.TaskPriority = TaskPriority
        
    def setID(self,ID):
        self.TaskID = ID
    
    def setType(self,Type):
        self.TaskType = Type
        
    def setPriority(self,Priority):
        self.TaskPriority = Priority
    



class Analyst(object):
    
    def __init__(self,AnalystName,AnalystPreference):
        self.AnalystName = AnalystName
        self.AnalystPreference = AnalystPreference
    
    def setName(self,Name):
        self.AnalystName = Name
    
    def setPreference(self,Preference):
        self.AnalystPreference = Preference



class TaskScheduler(object):

    def __init__(self):

        self.UrgentTaskList = []
        self.HighTaskList = []
        self.MediumTaskList = []
        self.LowTaskList = []

        self.TaskList = [self.UrgentTaskList,self.HighTaskList,self.MediumTaskList,self.LowTaskList]
        self.AnalystList = []
        self.TaskSequence = ['URGENT','HIGH','MEDIUM','LOW']


    def insertTask(self,TaskType,TaskID,TaskPriority):
        TaskSequenceNum = self.TaskSequence.index(TaskPriority)
        self.TaskList[TaskSequenceNum].append(Task(TaskType,TaskID,TaskPriority))
    
    def insertAnalyst(self,AnalystName,AnalystPreference):
        self.AnalystList.append(Analyst(AnalystName,AnalystPreference))

    def Assign(self):

        for singleTaskList in self.TaskList:
            for currentTask in singleTaskList:
                for currentAnalyst in self.AnalystList:
                    
                    if currentTask.TaskType in currentAnalyst.AnalystPreference:
                        singleTaskList.remove(currentTask)
                        self.AnalystList.remove(currentAnalyst)
                        print(str(currentTask.TaskId)+' -> '+str(currentAnalyst.AnalystName))
                    
                    else:
                        print(str(currentTask.TaskID)+' -> None')