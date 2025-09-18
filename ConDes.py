class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("File opened.")

    def write_data(self, data):
        self.file.write(data)
        print("Data written to file.")

    def __del__(self):  # Destructor
        self.file.close()
        print("File closed.")

fh = FileHandler("test.txt")
fh.write_data("Hello, World!")

del fh # Gọi hàm hủy, __del__ được gọi tự động