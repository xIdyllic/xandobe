from python_hosts import Hosts, HostsEntry
import logging, os, exception

target_host = Hosts()
logger = logging

logger.basicConfig(filename="adobe_patcher.log", filemode='a', level=logger.INFO)


def add_entry(ip_type, ip_address, name):
    new_entry = HostsEntry(entry_type=ip_type, address=ip_address, names=[name])
    target_host.add([new_entry])
    target_host.write()


def import_file_entry(file_path):
    file = target_host.import_file(file_path)
    target_host.add([file])
    target_host.write()


def get_hosts():
    amount = target_host.determine_hosts_path(platform='win')
    try:
        if os.path.isdir(amount) and os.path.exists(amount):
            logger.info(amount, " - Path and file exists.")
    except IOError as fileErr:
        logging.error(fileErr)
        print("There was an error, I have to exit now, sorry. Please check adobe_patcher.log")

