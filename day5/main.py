def extract_data() -> tuple[list[str], list[list[str]]]:
    with open("day5/input.txt", "r") as file:
        raw_rules, _, raw_updates = file.read().partition("\n\n")
        rules = raw_rules.split("\n")
        updates: list[list[str]] = []
        for raw_update in raw_updates.split("\n"):
            updates.append(raw_update.split(","))

        return rules, updates


def set_rules(rules: list[str]) -> dict[str, set[str]]:
    rules_dict: dict[str, set[str]] = {}
    for rule in rules:
        before, _, after = rule.partition("|")
        if before in rules_dict:
            rules_dict[before].add(after)
        else:
            rules_dict[before] = {after}

    return rules_dict


def validate_update(update: list[str], rules_dict: dict[str, set[str]]) -> bool:
    for i in range(len(update) - 1):
        if update[i] not in rules_dict:
            return False

        after_set = rules_dict[update[i]]
        if update[i + 1] not in after_set:
            return False

    return True


def sum_valid_updates_middle_page_numbers(
    updates: list[list[str]], rules_dict: dict[str, set[str]]
) -> None:
    total = 0
    for update in updates:
        if validate_update(update, rules_dict):
            total += int(update[len(update) // 2])

    print(f"Sum of middle page numbers of valid updates: {total}")


def reorder_update(update: list[str], rules_dict: dict[str, set[str]]) -> list[str]:
    rank: dict[str, int] = {}
    for page_1 in update:
        rank[page_1] = 0
        if page_1 not in rules_dict:
            continue

        for page_2 in update:
            if page_1 == page_2:
                continue

            if page_2 in rules_dict[page_1]:
                rank[page_1] += 1

    return [
        page for page, _ in sorted(rank.items(), key=lambda item: item[1], reverse=True)
    ]


def sum_reordered_invalid_updates_middle_page_numbers(
    updates: list[list[str]], rules_dict: dict[str, set[str]]
) -> None:
    total = 0
    for update in updates:
        if validate_update(update, rules_dict):
            continue

        update = reorder_update(update, rules_dict)
        total += int(update[len(update) // 2])

    print(f"Sum of middle page numbers invalid updates: {total}")


def main():
    rules, updates = extract_data()
    rules_dict = set_rules(rules)
    sum_valid_updates_middle_page_numbers(updates, rules_dict)
    sum_reordered_invalid_updates_middle_page_numbers(updates, rules_dict)


main()
