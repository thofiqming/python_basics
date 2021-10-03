# copy file content and crate new one with file name ending with _copy
def copy_a_file(file_path):
    with open(file_path, 'r') as fr:
        file_content = fr.read()
        with open(f'{file_path}_copy', 'w') as fw:
            fw.write(file_content)


copy_a_file('test.txt')
