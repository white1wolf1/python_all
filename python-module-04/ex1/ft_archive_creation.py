import sys


def ft_archive_creation() -> None:
    if len(sys.argv) == 1:
        print("No file provided!")
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        file_name_arg = sys.argv[1]
        file_fd = None
        if file_name_arg:
            try:
                file_fd = open(file_name_arg, "r")
                print("=== Cyber Archives Recovery & Preservation ===")
                print(f"Accessing file '{file_name_arg}'")
                print("---\n")
                readed_file = (file_fd.read())
                print(readed_file, "\n")
                print("---")
                file_fd.close()
                print(f"File '{file_name_arg}' closed.")
            except PermissionError as error_e:
                print("=== Cyber Archives Recovery & Preservation ===")
                print(f"Accessing file '{file_name_arg}'")
                print(f"Error opening file '{file_name_arg}':", error_e)
                if file_fd is not None:
                    file_fd.close()
                return
            except FileNotFoundError as error_e:
                print("=== Cyber Archives Recovery & Preservation ===")
                print(f"Accessing file '{file_name_arg}'")
                print(f"Error opening file'{file_name_arg}': ", error_e)
                if file_fd is not None:
                    file_fd.close()
                return
            except OSError as error_e:
                print("=== Cyber Archives Recovery & Preservation ===")
                print(f"unexpexted error has accured : {error_e} ")
                if file_fd is not None:
                    file_fd.close()
                return
            except NameError as error_e:
                print(error_e)
                if file_fd is not None:
                    file_fd.close()
                return

            try:
                print("Transform data:")
                print("---\n")
                file_fd = open(file_name_arg, "r+")
                readed_file = (file_fd.read())
                new_content = list()
                for x in readed_file.splitlines():
                    x = x.strip() + "#" + "\n"
                    new_content.append(x)
                    print(x, end="")
                print()
                print("---")
                input_file_name = input("Enter new file name (or empty):")
                if not input_file_name:
                    print("Not saving data.")
                    return
                print(f"Saving data to '{input_file_name}'.")
                file_fd = open(input_file_name, "w")
                for line in new_content:
                    file_fd.write(line)
                print(f"Data saved in file '{input_file_name}'.")
            except OSError as error_e:
                print(" unexpexted error has accured", error_e)
            except NameError as error_e:
                print(error_e)
            finally:
                if file_fd.closed is False:
                    file_fd.close()


if __name__ == "__main__":
    ft_archive_creation()
