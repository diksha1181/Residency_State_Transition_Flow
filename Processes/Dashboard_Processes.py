from Functions.Dashboard_Functions import DashboardFunctions

class DashboardProcesses:

    def __init__(self, dashboard: DashboardFunctions):     
        self.dashboard = dashboard


    def run_dash(self):
        
        self.dashboard.verify_draft()