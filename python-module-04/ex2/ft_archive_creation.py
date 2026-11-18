def secure_archive(file_name: str, action: str = "Read", context: str = "") -> tuple:
    if not file_name or file_name == "":
        return (False, "File name cannot be empty")
    if action and action.capitalize() not in ("Write", "Read") :
        return (False, "incorrect input please try again")
    elif action.capitalize() == "Write" or action.capitalize() == "Read":
        bool_tf = None
        tuple_return = tuple()
        action = action.capitalize()

        if action == "Write":
            action ="w"
        elif action == "Read":
            action = "r"
        try:
            with open(file_name,action) as file:
                if action == "r":
                    readed_file = file.read()
                    bool_tf = True
                    print("Using'secure_archive' to read from a regular file:")
                    tuple_return = (bool_tf, readed_file)

                if action == "w":
                    if context:
                        print("Using'secure_archive' to write previous content to a new file:")
                        file.write(context)
                        bool_tf = True
                        tuple_return = (bool_tf, "Content successfully written to file")
                    else:
                        bool_tf = False
                        tuple_return = (bool_tf, "there is nothing to write")
        except FileNotFoundError as error_e:
            if action == "r":
                print("Using'secure_archive' to read from a nonexistent file:")
            return (False, str(error_e))
        except PermissionError as error_e:
            if action == "r":
                print("Using'secure_archive' to read from an inaccessible file:")
            return (False, str(error_e))
        except OSError as error_e:
            return (False, str(error_e))
        return tuple_return
    else:
        return (False, "incorrect input please try again")


def main() -> None:
    print("=== Cyber Archives Security ===")
    


if __name__ == "__main__":
    main()