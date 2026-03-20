from Functions.State_Change_Functions import StateChangeFunctions
from Functions.Dashboard_Functions import DashboardFunctions


class StateChangeProcesses:

    def __init__(self, state: StateChangeFunctions, dashboard: DashboardFunctions):     
        self.state = state
        self.dashboard = dashboard

    def run_state(self):    
        self.state.Draft_To_Ip()
        self.dashboard.verify_status()
        self.state.IP_To_Wait()
        self.dashboard.verify_status()
        self.state.Wait_To_IP()
        self.dashboard.verify_status()
        self.state.IP_To_Pre()
        self.state.back()
        self.dashboard.verify_status()
        

      