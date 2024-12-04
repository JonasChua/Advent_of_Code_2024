from re import findall


def extract_data() -> str:
    with open("day3/input.txt", "r") as file:
        return file.read()


def extract_instructions(data: str) -> None:
    mul_pattern = r"mul\((\d+)\,(\d+)\)"
    matches = findall(mul_pattern, data)
    result = sum(int(num_1) * int(num_2) for num_1, num_2 in matches)
    print(f"Result = {result}")


def extract_enabled_instructions(data: str) -> None:
    mul_pattern = r"mul\((\d+)\,(\d+)\)"
    enable_pattern = r"(do\(\)|don't\(\))"
    enabled = True
    result = 0
    matches = findall(f"{mul_pattern}|{enable_pattern}", data)
    for num_1, num_2, command in matches:
        if num_1 and num_2 and enabled:
            result += int(num_1) * int(num_2)

        elif command == "do()":
            enabled = True

        elif command == "don't()":
            enabled = False

    print(f"Enabled result = {result}")


def main():
    data = extract_data()
    extract_instructions(data)
    extract_enabled_instructions(data)


main()
