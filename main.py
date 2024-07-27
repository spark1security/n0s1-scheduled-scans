import pathlib

here = pathlib.Path(__file__).parent.resolve()  # current path


def get_readme():
    file = here / "README.md"
    return file.read_text()


if __name__ == "__main__":
    print(get_readme())
