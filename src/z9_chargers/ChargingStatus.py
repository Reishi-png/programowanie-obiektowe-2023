#ChargingStatus
#- OPEN
#- ERROR
#- FINISHED


class ChargingStatus():
    
    def __init__(self):
        self.currentstatus = "OPEN"
    
    def get_status(self):
        return self.currentstatus
    
    def change_status(self, new_status):
        if new_status == "OPEN" or new_status == "ERROR" or new_status == "FINISHED":
            self.currentstatus = new_status
        else:
            self.currentstatus == "ERROR"
            
    def get_possible_statuses(self):
        print("OPEN,ERROR,FINISHED")
    

