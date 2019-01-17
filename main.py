import hosts_file


class Main():
    hosts = hosts_file

    def run(self):
        while True:
            try:
                if Menu(1):
                    print("You selected 1, initiating")
                    self.hosts.import_file_entry('hosts_append')
                    break
                if Menu(2):
                    print("You selected 2")
                if Menu(3):
                    print("You selected 3")
                if Menu(4):
                    print("You selected 4")
                if Menu(5):
                    print("You selected 5")
                if Menu(6):
                    print("You selected 6")
                else:
                    print("You didn't select a value, exiting.")
                    break
            except ValueError as val:
                print("Expected int, received " + str(val))


def Menu(menu_choice):
        print("""
        [1] - Add Host Entries\n
        [2] - Disable Adobe Services\n
        [3] - Replace AMTLIB.dll\n
        [4] - Edit Firewall\n
        [5] - Disable Adobe Startup applications\n
        [6] - Perform complete patch (automatically goes from 1 through 5 for you)\n""")
        menu_choice = int(input("Select action to perform via integer: "))
        return menu_choice


if __name__ == "__main__":
    Main().run()
