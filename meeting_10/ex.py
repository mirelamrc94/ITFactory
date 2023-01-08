
class File:

    def __init__(self, filename, mode):
        print("File.__init__")
        self.file_obj = open(filename, mode)

    def __enter__(self):
        print("File.__enter__")
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("File.__exit__")
        self.file_obj.close()

if __name__ == "__main__":

    print("===Entering <<with>> context===")
    with File("test1.txt", "r") as f1:
        content = f1.read()
        print(type(content))
        print(content)
    print("===Exiting <<with>> context===")

    with File("test2.txt", "w") as f2:
        f2.write("Hello second file!")
