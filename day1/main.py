def extract_data() -> tuple[list[int], list[int]]:
    list_1: list[int] = []
    list_2: list[int] = []
    with open("day1/input.txt", "r") as file:
        for line in file:
            nums = line.split()
            list_1.append(int(nums[0]))
            list_2.append(int(nums[1]))

    return list_1, list_2


def get_total_distance(list_1: list[int], list_2: list[int]) -> None:
    distance = 0
    for i, id_1 in enumerate(list_1):
        difference = abs(id_1 - list_2[i])
        distance += difference

    print(f"Total distance: {distance}")


def count_frequency(data: list[int]) -> dict[int, int]:
    frequency: dict[int, int] = {}
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


def get_similarity_score(data: list[int], frequency: dict[int, int]) -> None:
    score = 0
    for num in data:
        if num in frequency:
            score += num * frequency[num]

    print(f"Similarity score: {score}")


def main() -> None:
    list_1, list_2 = extract_data()
    list_1.sort()
    list_2.sort()
    get_total_distance(list_1, list_2)
    frequency = count_frequency(list_1)
    get_similarity_score(list_2, frequency)


main()
