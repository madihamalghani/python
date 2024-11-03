# python 3.10  feature:
def handle_command(command):
    match command:
        case "start":
            print("Starting the process...")
        case "stop":
            print("Stopping the process...")
        case "pause":
            print("Pausing the process...")
        case _:
            print("Unknown command.")
handle_command('start')
handle_command('I am irrelevent')