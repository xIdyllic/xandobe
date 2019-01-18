from python_hosts import *
import logging, os, exception


class Entries:
    target_host = Hosts()
    logger = logging
    logger.basicConfig(filename="adobe_patcher.log", filemode='a', level=logger.INFO)

    def prompt_entry(self):
        user_prompt = int(input("""\nWhat would you like to do?
    [1] - Custom host entry
    [2] - Import .txt file containing host entries\n
    Select integer [1, 2]: """))
        if user_prompt == 1:
            self.add_custom_entry()
        if user_prompt == 2:
            file_path = input("Enter the path of the custom .txt file (no need for full path if file is in same directory as this tool): ")
            self.import_file_entry(file_path)

    def add_custom_entry(self):
        ip_entry, name_entry = (input("Type your input, example: 127.0.0.1 localhost (include the space between IP Address and name.)\nEntry: ").split())
        if utils.is_ipv4(ip_entry):
            try:
                new_entry = HostsEntry(entry_type='ipv4', address=ip_entry, names=[name_entry])
                self.target_host.add([new_entry])
                self.target_host.write()
            except exception.UnableToWriteHosts() as writefail:
                logging.error(writefail)
        elif ip_entry is not utils.is_ipv4(ip_entry):
            print("\nIP Address is not an IPv4 Address. Please try again.\n")
            self.add_custom_entry()

    def import_file_entry(self, file_path):
        file = self.target_host.import_file(file_path)

    def get_hosts(self):
        amount = self.target_host.determine_hosts_path(platform='win')
        try:
            if os.path.isdir(amount) and os.path.exists(amount):
                self.logger.info(amount, " - Path and file exists.")
        except IOError as fileErr:
            logging.error(fileErr)
            print("There was an error, I have to exit now, sorry. Please check adobe_patcher.log")
