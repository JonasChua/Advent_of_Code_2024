def extract_data() -> list[list[str]]:
    map_data: list[list[str]] = []
    with open("day6/input.txt", "r") as file:
        for line in file:
            map_data.append(list(line.removesuffix("\n")))

        return map_data


def find_guard_position(map_data: list[list[str]]) -> tuple[int, int]:
    i = j = 0
    for i, row in enumerate(map_data):
        if "^" in row:
            j = row.index("^")
            break

    return i, j


def in_map(map_data: list[list[str]], i: int, j: int) -> bool:
    if 0 <= i < len(map_data) and 0 <= j < len(map_data[i]):
        return True

    return False


def update_position(
    position: tuple[int, int], direction: tuple[int, int]
) -> tuple[int, int]:
    return tuple(map(lambda x, y: x + y, position, direction))  # type: ignore


def find_path(map_data: list[list[str]], cur_pos: tuple[int, int]) -> None:
    move_dir = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    change_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}
    distinct_pos = 0
    while True:
        direction = map_data[cur_pos[0]][cur_pos[1]]
        next_pos = update_position(cur_pos, move_dir[direction])
        if not in_map(map_data, *next_pos):
            distinct_pos += 1
            break

        match map_data[next_pos[0]][next_pos[1]]:
            case ".":
                map_data[next_pos[0]][next_pos[1]] = direction
                map_data[cur_pos[0]][cur_pos[1]] = "X"
                cur_pos = next_pos
                distinct_pos += 1
            case "X":
                map_data[next_pos[0]][next_pos[1]] = direction
                map_data[cur_pos[0]][cur_pos[1]] = "X"
                cur_pos = next_pos
            case "#":
                new_direction = change_dir[direction]
                map_data[cur_pos[0]][cur_pos[1]] = new_direction

    for row in map_data:
        print("".join(row))

    print(f"Distinct positions visited: {distinct_pos}")


def main():
    map_data = extract_data()
    current_position = find_guard_position(map_data)
    find_path(map_data, current_position)


main()
