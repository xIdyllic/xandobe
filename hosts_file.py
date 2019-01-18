from python_hosts import Hosts, HostsException, HostsEntry, utils, exception
import logging, os, hashlib


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
            if utils.is_readable(file_path):
                self.import_file_entry(file_path)
            if file_path is not utils.is_readable(file_path):
                try_again = input("Cannot find file path! Would you like to try again? [y/n]: ")
                if try_again == 'y':
                    os.system('cls')
                    self.prompt_entry()
                elif try_again == 'n':
                    exit()

    def add_custom_entry(self):
        ip_entry, name_entry = (input("Type your input, example: 127.0.0.1 localhost (include the space between IP Address and name.)\nEntry: ").split())
        if utils.is_ipv4(ip_entry):
            try:
                new_entry = HostsEntry(entry_type='ipv4', address=ip_entry, names=[name_entry])
                self.target_host.add([new_entry])
                self.target_host.write()
            except Exception as writefail:
                print("\nCustom entry failed, an exception was caught. Could be a permissions error >> Check adobe_patcher.log")
                logging.exception(writefail)
        elif ip_entry is not utils.is_ipv4(ip_entry):
            print("\nIP Address is not an IPv4 Address. Please try again.\n")
            self.add_custom_entry()

    def import_file_entry(self, file_path):
        try:
            self.target_host.import_file(file_path)
        except Exception as writefail:
            print("File import failed, an exception was caught. Could be a permissions error >> check adobe_patcher.log")
            logging.exception(writefail)

    def get_hosts(self):
        try:
            path = self.target_host.determine_hosts_path()
            if path:
                print("File exists!")
                logging.debug(path)
        except Exception as fileErr:
            logging.error(fileErr)
            print("File not found! Check adobe_patcher.log")

    def remove_duplicate_entries(self):
        input_file_path = os.getcwd() + "adobe_patcher.log"
        output_file_path = os.getcwd()
        lines_hash = set()
        output_file = open(output_file_path, 'w+')

        for line in open(input_file_path, 'r'):
            hash_val = hashlib.md5(line.rstrip())
            if hash_val not in lines_hash:
                output_file.write(line)
                lines_hash.add(hash_val)
        output_file.close()

