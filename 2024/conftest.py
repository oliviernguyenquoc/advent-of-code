# conftest.py
import re
from rich.console import Console
from rich.table import Table
from rich import box
from collections import defaultdict

# Constants for test statuses
PASSED = "✅"
FAILED = "❌"
TIMEOUT = "⏳"
TIMEOUT_SECONDS = "[yellow]>2s[/yellow]"
NA = "[red]NA[/red]"

test_results = defaultdict(
    lambda: {
        "part1_status": None,
        "part1_time": None,
        "part2_status": None,
        "part2_time": None,
    }
)


def parse_year_day_part(nodeid: str):
    """
    Given a nodeid like '2024/day24/test_day24.py::test_part1[param0]',
    return (year='2024', day='24', part=1 or 2).
    """
    # Split nodeid at '::' to separate file-part from function-part
    file_part, func_part = nodeid.split("::", 1)
    # file_part might be '2024/day24/test_day24.py'
    segments = file_part.split("/")

    # Expect segments = ['2024', 'day24', 'test_day24.py']
    year = segments[0]  # e.g. '2024'
    day_folder = segments[1]  # e.g. 'day24'

    # Extract the numeric part from 'day24'
    match = re.search(r"\d+", day_folder)
    day = match.group(0) if match else day_folder  # '24'

    # Decide whether it's test_part1 or test_part2
    # (func_part could be 'test_part1[param0]' or 'test_part2')
    if "test_part1" in func_part:
        part = 1
    elif "test_part2" in func_part:
        part = 2
    else:
        part = 0  # Not recognized as part1/part2
    return year, day, part


def pytest_runtest_logreport(report):
    """
    Called after each test phase (setup, call, teardown).
    We only care about the 'call' phase to see pass/fail/timeout and duration.
    """
    if report.when != "call":
        return

    # Parse (year, day, part) from this test’s nodeid
    year, day, part = parse_year_day_part(report.nodeid)

    # Not a part1 or part2 test—ignore
    if part not in (1, 2):
        return

    status, duration = determine_status_and_duration(report)
    key = (year, day)
    if part == 1:
        test_results[key]["part1_status"] = status
        test_results[key]["part1_time"] = duration
    elif part == 2:
        test_results[key]["part2_status"] = status
        test_results[key]["part2_time"] = duration


def determine_status_and_duration(report):
    """
    Determine the status and duration of a test report.
    """
    if report.outcome == "passed":
        return PASSED, report.duration
    if report.outcome == "failed":
        if "Failed: Timeout >" in str(report.longrepr):
            return TIMEOUT, ">2s"
        return FAILED, report.duration
    return NA, None


def pytest_terminal_summary(terminalreporter):
    """
    At the end of the test run, print a custom summary table using Rich.
    """
    if not test_results:
        return  # No data collected

    # We can write a "title" above the table if desired
    terminalreporter.write_sep("=", "Advent of Code Summary")

    # Create a console that writes to the same output file as Pytest
    # so the table appears in the normal Pytest output stream.
    console = Console(file=terminalreporter._tw._file)

    table = create_summary_table()

    # Sort results by (year, numeric day) for consistent ordering
    sorted_items = sorted(test_results.items(), key=lambda x: (x[0][0], int(x[0][1])))

    # Populate table rows
    for (year, day), data in sorted_items:
        table.add_row(
            str(year),
            str(day),
            data["part1_status"] or NA,
            data["part2_status"] or NA,
            format_time(data["part1_time"]),
            format_time(data["part2_time"]),
        )

    # Print the table via Rich
    console.print(table)

    # Optional: Still print any TIMEOUTED TESTS section, if you like:
    timeouts = terminalreporter.stats.get("timeout", [])
    if timeouts:
        terminalreporter.write_sep("=", "TIMEOUTED TESTS", yellow=True)
        for rep in timeouts:
            terminalreporter.write_line(f"{rep.nodeid}")
        terminalreporter.write_line("")


def create_summary_table():
    """
    Create a Rich table for the summary.
    """
    table = Table(title="Advent of Code Results", show_lines=True)
    table.box = box.ROUNDED
    table.add_column("Year", justify="center", style="bold cyan")
    table.add_column("Day", justify="center", style="bold magenta")
    table.add_column("Part 1", justify="center", style="bold green")
    table.add_column("Part 2", justify="center", style="bold green")
    table.add_column("Exec. Time Part 1", justify="center", style="yellow")
    table.add_column("Exec. Time Part 2", justify="center", style="yellow")
    return table


def format_time(time):
    """
    Format time for display.
    """
    if time not in (None, ">2s"):
        time_str = f"[green]{time*1000:.0f}ms[/green]"
    elif time is not None:
        time_str = "[yellow]>2s[/yellow]"
    else:
        time_str = NA
    return time_str


def pytest_report_teststatus(report, config):
    """
    Hook to modify how pytest reports test results in the terminal.
    If it's a timeout, we return ("timeout", "T", "TIMEOUT").
    """
    if report.when == "call" and report.failed:
        if "Failed: Timeout >" in str(report.longrepr):
            # Use "⏳" in the progress line, and "TIMEOUT" in the verbose summary
            return ("timeout", "T", ("TIMEOUT", {"yellow": True}))
    return default_report_teststatus(report)


def default_report_teststatus(report):
    """
    Helper function that returns the default pytest behavior for the status tuple.
    """
    outcome = report.outcome
    short_letter = {
        "passed": ".",
        "failed": "F",
        "skipped": "s",
    }.get(outcome, "?")
    return (outcome, short_letter, outcome.upper())
