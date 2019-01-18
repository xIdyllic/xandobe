import hosts_file


class Main:

    hosts = hosts_file.Entries()

    def launch(self):
        while True:
            try:
                if self.menu(1):
                    self.hosts.prompt_entry()
                    break
                elif self.menu(2):
                    break
                elif self.menu(3):
                    break
                elif self.menu(4):
                    break
                elif self.menu(5):
                    break
                elif self.menu(6):
                    break
                else:
                    print("Something happened, exiting.")
                    break
            except ValueError as val:
                print("Expected int, received " + str(val) + "\nGoing back to menu.")

    def menu(self, menu_choice):
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
    Main().launch()
