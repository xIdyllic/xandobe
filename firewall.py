from python_hosts import utils
import logging, subprocess, os, ctypes

'''Powershell will be run through subprocess module to allow diversity for rules and net administration.
netsh was the first consideration until finding out that they might be deprecating it in future Windows versions:

"In future versions of Windows, Microsoft might remove the Netsh functionality
for Windows Firewall with Advanced Security.

Microsoft recommends that you transition to Windows PowerShell if you currently
use netsh to configure and manage Windows Firewall with Advanced Security."
 
This is preferable, though.'''


class Firewall:

    system = os
    subproc = subprocess
    logger = logging
    logger.basicConfig(filename="adobe_patcher.log", filemode='a', level=logging.INFO)
    ps_file_inbound = 'powershell/add_rule_inbound.ps1'
    ps_file_outbound = 'powershell/add_rule_outbound.ps1'

    '''Much love, servervault. https://serverfault.com/questions/11320/command-line-safety-tricks/29261#29261'''

    def prompt_firewall(self):
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                self.logger.info(" User is admin, adding inbound firewall rule...")
                try:
                    self.subproc.Popen(["powershell.exe", self.ps_file_inbound], stdout=self.subproc.PIPE)
                    self.logger.log(self.logger.INFO, " Firewall rule added to inbound. Adding to outbound...")
                    try:
                        self.logger.info("Attempting to add Outbound")
                        self.subproc.Popen(['powershell.exe', self.ps_file_outbound], stdout=self.subproc.PIPE)
                    except (PermissionError, OSError) as err:
                        self.logger.exception(err)
                except (PermissionError, OSError) as err:
                    self.logger.exception(err)
            else:
                print("Permission error! Check the log file. Exiting.")
                self.logger.error(" User is not admin, exiting.")
                exit()
        except (OSError, OverflowError, SystemError) as error:
            self.logger.exception(error)

    def get_path(self, paths, executable=''):
        adobe_paths = []
        for dir in self.system.walk(paths):
            print(dir)
            exit()


