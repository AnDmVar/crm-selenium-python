def read(directory, filename):
    with open(directory / filename) as file:
        return file.read()
