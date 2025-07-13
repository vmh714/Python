def process_command(command):
    match command:
        case "help":
            print("Showing help...")
            return True
        case "quit":
            print("Quitting...")
            return False
        case ("load", filename):
            print(f"Loading file: {filename}")
            return True
        case ("save", filename):
            print(f"Saving to file: {filename}")
            return True
        case _:
            print("Unknown command")
            return True
