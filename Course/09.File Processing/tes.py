from pathlib import Path

UNIT_DIR = Path(__file__).parent
DATA_DIR = UNIT_DIR / "data"
notes_path = DATA_DIR / "notes.txt"
#### so we adress this file as being in the parent file of 0.9U and we also say that in 
#### in parent of this file there is abother folder called data, which has notes inside
print(UNIT_DIR)
print(DATA_DIR)
print(notes_path)
###c:\Users\Win PRO\Documents\GitHub\compsci_2025-2027\Course\09.File Processing
###c:\Users\Win PRO\Documents\GitHub\compsci_2025-2027\Course\09.File Processing\data
###c:\Users\Win PRO\Documents\GitHub\compsci_2025-2027\Course\09.File Processing\data\notes.txt
#In the terminal:
##cd(.name, ..)
##ls(list)

#to open it:

with open(notes_path, "r") as f:
    print(f.read())

with open(notes_path, "a") as f:
    f.write("hello")

###Mode Description

#‘r’	Read-only. Raises I/O error if file doesn't exist.
#‘r+’	Read and write. Raises I/O error if the file does not exist.
#‘w’	Write-only. Overwrites file if it exists, else creates a new one.(deletes previous)
#‘w+’	Read and write. Overwrites file or creates new one. 
#‘a’	Append-only. Adds data to end. Creates file if it doesn't exist.
#‘a+’	Read and append. Pointer at end. Creates file if it doesn't exist.

###with open(Path(__file__).parent/"data/purchase.txt", "Mode") as f: