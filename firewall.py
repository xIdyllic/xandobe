from python_hosts import utils
import logging, subprocess

'''Powershell will be run through subprocess module to allow diversity for rules and net administration.
netsh was the first consideration until finding out that they might be deprecating it in future Windows versions:

"In future versions of Windows, Microsoft might remove the Netsh functionality
for Windows Firewall with Advanced Security.

Microsoft recommends that you transition to Windows PowerShell if you currently
use netsh to configure and manage Windows Firewall with Advanced Security."
 
This is preferable, though.'''

class Firewall:

    subproc = subprocess
    logger = logging
    logger.basicConfig(filename="adobe_patcher.log", filemode='a', level=logging.INFO)

    ps_commands = ['$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())',
                   '$currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)']

    '''Much love, servervault. https://serverfault.com/questions/11320/command-line-safety-tricks/29261#29261'''

    def prompt_firewall(self):
        try:
            with open('admin_check', 'w+') as io:
                for command in self.ps_commands:
                    io.write("%s\n" % command)
                io.close()
        except (PermissionError, OSError, AttributeError) as error:
            self.logger.exception(error)



