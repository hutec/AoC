with open("../inputs/02", "r") as f:
    reports = f.readlines()


def is_increasing(report: list[int]) -> bool:
    return sorted(report) == report


def is_decreasing(report: list[int]) -> bool:
    return sorted(report, reverse=True) == report


def level_diff_in_range(report: list[int], lower_bound: int, upper_bound: int) -> bool:
    # Difference between adjacent levels
    diff = list(map(lambda x: abs(x[1] - x[0]), zip(report, report[1:])))
    return all(lower_bound <= x <= upper_bound for x in diff)


def check_report(report: list[int]) -> bool:
    return (is_increasing(report) or is_decreasing(report)) and level_diff_in_range(
        report, 1, 3
    )


safe_count = 0
for report in reports:
    report = list(map(int, report.split()))
    if check_report(report):
        safe_count += 1

print(safe_count)

safe_count = 0
for report in reports:
    report = list(map(int, report.split()))
    for skip_level in range(len(report)):
        report_with_skipped_level = report[:skip_level] + report[skip_level + 1 :]
        if check_report(report_with_skipped_level):
            safe_count += 1
            break

print(safe_count)
