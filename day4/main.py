def extract_data() -> list[str]:
    with open("day4/input.txt", "r") as file:
        return file.read().split("\n")


def is_valid_index(i: int, j: int, m: int, n: int) -> bool:
    return 0 <= i < m and 0 <= j < n


def search_matching_words(i: int, j: int, y: int, x: int, data: list[str]) -> bool:
    word = "XMAS"
    m = len(data)
    n = len(data[0])
    for k, c in enumerate(word):
        new_i = i + k * y
        new_j = j + k * x
        if not (0 <= new_i < m and 0 <= new_j < n):
            return False

        if data[new_i][new_j] != c:
            return False

    return True


def count_xmas_appearance(data: list[str]) -> None:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != "X":
                continue

            for y, x in directions:
                count += 1 if search_matching_words(i, j, y, x, data) else 0

    print(f"Number of 'XMAS' appearance: {count}")


def count_x_mas_appearance(data: list[str]) -> None:
    count = 0
    m = len(data)
    n = len(data[0])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if data[i][j] != "A":
                continue

            pattern = (
                f"{data[i-1][j-1]}{data[i-1][j+1]}{data[i+1][j-1]}{data[i+1][j+1]}"
            )
            if pattern in {"MMSS", "MSMS", "SMSM", "SSMM"}:
                count += 1

    print(f"Number of 'X-MAS' appearance: {count}")


def main():
    data = extract_data()
    count_xmas_appearance(data)
    count_x_mas_appearance(data)


main()
