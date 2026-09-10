from ase import io

file_path = r"C:\Users\Win PRO\Documents\GitHub\compsci_2025-2027\Cute\molecule.xyz"

# Write a simple Hydrogen molecule to the file
with open(file_path, "w", encoding="utf-8") as f:
    f.write("""2
Hydrogen molecule
H 0.0 0.0 0.0
H 0.0 0.0 0.74
""")

# Now read it with ASE
atoms = io.read(file_path)
print(atoms)
