from python_hosts import utils
import logging, subprocess, os

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
    temp_folder = os.getenv('temp')

    ps_file = "{}\\xandobe\\admin_check.ps1".format(temp_folder)
    ps_script = subproc.Popen(["powershell.exe", ps_file], stdout=subproc.PIPE)
    ps_commands = ['$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())',
                   '$currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)']

    '''Much love, servervault. https://serverfault.com/questions/11320/command-line-safety-tricks/29261#29261'''

    def prompt_firewall(self):
        try:
            if not os.path.exists(self.temp_folder + '\\xandobe'):
                os.mkdir(self.temp_folder + '\\xandobe')
            else:
                with open(self.ps_file, "w+") as io:
                    for command in self.ps_commands:
                        io.write("%s\n" % command)
                        self.logger.info("PowerShell commands inserted into file C:\\admin_check.ps1 - Continuing")
                    io.close()
                output = self.ps_script.communicate()[0]
                if output.decode('ascii') == 'True':
                    pass # Add Firewall rules.
                if output.decode('ascii') == 'False':
                    print('False permissions! Check adobe_patcher.log for more details.')
                    self.logger.exception('You do not have the correct permissions! Returned false.')
                    raise PermissionError
                else:
                    print("Critical error, exiting.")
                    self.logger.critical("Something happened, exiting.") # Could keep this or leave the raise to do it's thing. We'll see.
                    exit()
        except (PermissionError, OSError, AttributeError) as error:
            print("There was an error. Most likely permissions. Check adobe_patcher.log")
            self.logger.exception(error)