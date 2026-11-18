import sys


def ft_ancient_text() -> None:
    if len(sys.argv) == 1:
        print("No file provided!")
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        fd_file = None
        file_name = sys.argv[1]
        if file_name:
            try:
                fd_file = open(file_name, "r",)
                print("=== Cyber Archives Recovery ===")
                print(f"Accessing file '{file_name}'")
                print("---")
                print()
                print(fd_file.read())
                print()
                print("---")
                print(f"File '{file_name}' closed.")
            except PermissionError as error_e:
                print("=== Cyber Archives Recovery ===")
                print(f"Accessing file '{file_name}'")
                print(f"Error opening file '{file_name}':", error_e)
            except FileNotFoundError as error_e:
                print("=== Cyber Archives Recovery ===")
                print(f"Accessing file '{file_name}'")
                print(f"Error opening file '{file_name}': ", error_e)
            except OSError as error_e:
                print("=== Cyber Archives Recovery ===")
                print(f"unexpected error has occurred: {error_e}")
            finally:
                if fd_file is not None:
                    fd_file.close()


if __name__ == "__main__":
    ft_ancient_text()
