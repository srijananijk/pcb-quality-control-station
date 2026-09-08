# pcb-quality-control-station

**Problem Statement:** CircuitWorks — PCB Quality Control Station
CircuitWorks runs an automated inspection station for printed circuit boards (PCBs). Each board is measured on a variable number of test points depending on board type, checked against a tolerance, and logged. The station needs to move off copy-pasted inspection code into clean, reusable functions — using return (not print) so results flow onward, supporting a default tolerance, safely handling a shared defect log without the mutable-default trap, and accepting variable extra board metadata.


**Task**: Write a Python script that does the following, in order:
Write inspect\_point(reading, target, tolerance=0.05) that returns True if abs(reading - target) <= tolerance, else False


Write inspect\_board(board\_id, defect\_log=None, \*readings, \*\*metadata) that:
- Fixes the mutable-default trap correctly: if defect\_log is None, create a brand-new empty list inside the function body
- Uses \*readings to accept a variable number of raw sensor readings per board (some boards have 3 test points, others have 2)
- Uses \*\*metadata to accept optional extra info like batch="B12" or line="L3" that not every call needs to supply
- Checks each reading against a fixed target of 5.0 using inspect\_point(), and .append()s board\_id to defect\_log for every failing reading
- Returns two values as a tuple — passed count and failed count — so the caller can unpack both at once


Call inspect\_board() twice for two different boards, explicitly sharing the same defect\_log list across both calls (not relying on the default) to prove the log accumulates correctly


On the second call, pass the batch and line keyword arguments in a different order than intended, to demonstrate that keyword-argument order doesn't matter


Print the pass/fail counts for each board (via tuple unpacking) and the final shared defect\_log

