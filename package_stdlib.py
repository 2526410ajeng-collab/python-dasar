import os
import json

print("Folder aktif:", os.path.basename(os.getcwd()))
print("JSON:", json.dumps({"nama": "Ajeng"}))
