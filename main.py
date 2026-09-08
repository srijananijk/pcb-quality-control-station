# ----- CircuitWorks: PCB Quality Control Station -----

def inspect_point(reading, target, tolerance=0.05):
    return abs(reading - target) <= tolerance


def inspect_board(board_id, defect_log=None, *readings, **metadata):
    # Fix for the mutable default trap: never default to a mutable container directly
    if defect_log is None:
        defect_log = []

    target = 5.0
    passed = 0
    failed = 0

    for reading in readings:
        if inspect_point(reading, target):
            passed += 1
        else:
            failed += 1
            defect_log.append(board_id)   # mutates the shared list directly

    print(f"Board {board_id} metadata: {metadata}")
    return passed, failed


# Shared defect log across both boards, passed explicitly (not via the default)
defect_log = []

p1, f1 = inspect_board("PCB-01", defect_log, 5.02, 4.90, 5.10, batch="B12")
# Keyword order swapped vs the call above — result is identical either way
p2, f2 = inspect_board("PCB-02", defect_log, 4.80, 5.01, line="L3", batch="B12")

print(f"PCB-01 -> Passed: {p1}, Failed: {f1}")
print(f"PCB-02 -> Passed: {p2}, Failed: {f2}")
print("Shared defect log:", defect_log)
print("The End")