
from orgparse.date import OrgDateRepeatedTask, OrgDateDeadline
from orgparse.node import OrgNode


data = [dict(
    heading='Pay the rent',
    todo='TODO',
    deadline=OrgDateDeadline((2005, 10, 1)),
    repeated_tasks=[
        OrgDateRepeatedTask((2005, 9, 1, 16, 10, 0), 'TODO', 'DONE'),
        OrgDateRepeatedTask((2005, 8, 1, 19, 44, 0), 'TODO', 'DONE'),
        OrgDateRepeatedTask((2005, 7, 1, 17, 27, 0), 'TODO', 'DONE'),
    ]
)]

# with open("03_repeated_tasks.org", "r") as infile:
#     lines = infile.readlines()

from orgparse import *
root = load("src/orgparse/tests/data/06_log_notes.org")
print(root[1].timestamp_log_notes[0])
# print(root[1].repeated_tasks)
