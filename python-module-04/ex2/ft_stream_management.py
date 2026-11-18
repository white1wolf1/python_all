import sys
from typing import IO, Optional


def ft_stream_management() -> None:
    if len(sys.argv) == 1:
        sys.stdout.write("No file provided!\n")
        sys.stderr.write("[STDERR] Usage: ft_stream_management.py <file>\n")
        return
    else:
        file_name_arg = sys.argv[1]
        file_fd: Optional[IO[str]] = None
        if file_name_arg:
            try:
                file_fd = open(file_name_arg, "r")
                sys.stdout.write("=== Cyber Archives Recovery &"
                                 " Preservation ===\n")
                sys.stdout.write(f"Accessing file '{file_name_arg}'\n")
                sys.stdout.write("---\n\n")
                readed_file = (file_fd.read())
                sys.stdout.write(readed_file + "\n")
                sys.stdout.write("---\n")
                file_fd.close()
                sys.stdout.write(f"File '{file_name_arg}' closed.\n")
            except PermissionError as error_e:
                sys.stdout.write("=== Cyber Archives Recovery"
                                 " & Preservation ===\n")
                sys.stdout.write(f"Accessing file '{file_name_arg}'\n")
                sys.stderr.write(f"[STDERR] Error opening file "
                                 f"'{file_name_arg}': {error_e}\n")
                if file_fd is not None:
                    file_fd.close()
                return
            except FileNotFoundError as error_e:
                sys.stdout.write("=== Cyber Archives Recovery"
                                 " & Preservation ===\n")
                sys.stdout.write(f"Accessing file '{file_name_arg}'\n")
                sys.stderr.write(f"[STDERR] Error opening file "
                                 f"'{file_name_arg}': {error_e}\n")
                if file_fd is not None:
                    file_fd.close()
                return
            except OSError as error_e:
                sys.stdout.write("=== Cyber Archives Recovery &"
                                 " Preservation ===\n")
                sys.stderr.write(f"[STDERR] unexpected error has occurred:"
                                 f" {error_e}\n")
                if file_fd is not None:
                    file_fd.close()
                return
            except NameError as error_e:
                sys.stderr.write(f"[STDERR] {error_e}\n")
                if file_fd is not None:
                    file_fd.close()
                return

            input_file_name = ""
            try:
                sys.stdout.write("\nTransform data:\n")
                sys.stdout.write("---\n\n")
                file_fd = open(file_name_arg, "r")
                readed_file = (file_fd.read())
                file_fd.close()
                new_content = []
                for line in readed_file.splitlines():
                    newline = line.rstrip() + "#" + "\n"
                    new_content.append(newline)
                    sys.stdout.write(newline)
                sys.stdout.write("\n")
                sys.stdout.write("---\n")
                sys.stdout.write("Enter new file name (or empty): ")
                sys.stdout.flush()
                input_file_name = sys.stdin.readline().strip()
                if not input_file_name:
                    sys.stdout.write("Not saving data.\n")
                    return
                sys.stdout.write(f"Saving data to '{input_file_name}'\n")
                file_fd = open(input_file_name, "w")
                for line in new_content:
                    file_fd.write(line)
                sys.stdout.write(f"Data saved in file '{input_file_name}'.\n")
            except OSError as error_e:
                sys.stderr.write(f"[STDERR] Error opening file "
                                 f"'{input_file_name}': {error_e}\n")
                sys.stdout.write("Data not saved.\n")
            except NameError as error_e:
                sys.stderr.write(f"[STDERR] {error_e}\n")
            finally:
                if file_fd is not None and file_fd.closed is False:
                    file_fd.close()


if __name__ == "__main__":
    ft_stream_management()
