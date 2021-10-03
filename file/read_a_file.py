# read complete file content
def read_a_file(file_path):
    with open(file_path) as fr:
        print(fr.read())


read_a_file('test.txt')


# read file using predefined chunks
def read_a_file_with_chunks(file_path):
    with open(file_path) as f:
        chunk_size = 100
        chunk = f.read(chunk_size)
        while len(chunk) > 0:
            print(chunk)
            chunk = f.read(chunk_size)


read_a_file_with_chunks("test.txt")