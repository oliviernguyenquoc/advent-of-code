

def is_safe(report):
    sorted_report = sorted(report)
    if report == sorted_report or report == sorted_report[::-1]:
        for i in range(1, len(report)):
            if abs(report[i] - report[i - 1]) > 3 or report[i] == report[i - 1]:
                return False
        return True
    return False


def is_safe_removing_1(report):
    sorted_report = sorted(report)
    if report == sorted_report or report == sorted_report[::-1]:
        for i in range(1, len(report)):
            if abs(report[i] - report[i - 1]) > 3 or report[i] == report[i - 1]:
                report_removed_i = report[:i] + report[i + 1 :]
                report_removed_i_1 = report[: i - 1] + report[i:]
                return is_safe(report_removed_i) or is_safe(report_removed_i_1)
        return True
    else:
        for i in range(0, len(report)):
            report_removed_i = report[:i] + report[i + 1 :]
            if is_safe(report_removed_i):
                return True

    return False


with open("./advent_of_code_2024/day2/input.txt", encoding="utf-8") as f:
    reports = f.read().splitlines()

reports = [list(map(int, report.split())) for report in reports]

safe_reports = sum([is_safe(report) for report in reports])
safe_reports_2 = sum([is_safe_removing_1(report) for report in reports])
print([p for p,v in enumerate(zip(
    [is_safe(report) for report in reports],
    [is_safe_removing_1(report) for report in reports])) if v[0]^v[1]])
print("Solution 1:", safe_reports)
print("Solution 2:", safe_reports_2)