def extract_data() -> list[list[int]]:
    data: list[list[int]] = []
    with open("day2/input.txt", "r") as file:
        for line in file:
            nums = line.split()
            data.append([int(num) for num in nums])

    return data


def validate_safe(report: list[int]) -> bool:
    increasing: bool | None = None
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if difference == 0 or abs(difference) > 3:
            return False

        if increasing is None:
            increasing = True if difference > 0 else False
            continue

        if difference < 0 and increasing is True:
            return False

        if difference > 0 and increasing is False:
            return False

    return True


def count_safe_levels(data: list[list[int]]) -> None:
    count = 0
    for report in data:
        if validate_safe(report) is True:
            count += 1

    print(f"Safe reports: {count}")


def validate_dampened_safe(report: list[int]) -> bool:
    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1 :]
        if validate_safe(temp_report) is True:
            return True

    return False


def count_dampened_safe_levels(data: list[list[int]]) -> None:
    count = 0
    for report in data:
        if validate_safe(report) is True:
            count += 1

        elif validate_dampened_safe(report) is True:
            count += 1

    print(f"Dampened safe reports: {count}")


def main() -> None:
    data = extract_data()
    count_safe_levels(data)
    count_dampened_safe_levels(data)


main()
