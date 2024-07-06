def read_lines(path: str) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file]
