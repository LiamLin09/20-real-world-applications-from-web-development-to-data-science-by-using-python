contents = ['Ryan is so bad.',
            'Ryan is pretty bad.',
            'Ryan is super bad.']

file_name = ['file1.txt', 'file2.txt', 'file3.txt']

for content, filename in zip(contents, file_name):
    file = open(f"files/{filename}", 'w')
    file.write(content)