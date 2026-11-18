kelas = {"siswa1": {"nama": "Ajeng", "nilai": 85}, "siswa2": {"nama": "Rina", "nilai": 90}}
print(kelas["siswa1"]["nama"])
print(kelas["siswa2"]["nilai"])
for kunci, data in kelas.items():
    print(kunci, "->", data["nama"], data["nilai"])
