import zipfile


def extract_archive(archive_paths, dest_dir):
    with zipfile.ZipFile(archive_paths, 'r') as archive:
        archive.extractall(dest_dir)


if __name__=="__main__":
    extract_archive(archive_paths="compressed.zip",
                    dest_dir='test')