import os
import subprocess

relative_path = "SastToolsEvaluation/semgrep-test-files"
print(os.getcwd())
for root, dirs, files in os.walk(os.path.join(os.getcwd(), relative_path, "semgrep-rules")):
    for file in files:
        if file[0] == ".":
            continue
        if not file.endswith(".yaml"):
            destfolder = root.replace("semgrep-rules", "")
            os.makedirs(destfolder, exist_ok=True)
            try:
                subprocess.run(["cp", os.path.join(root, file), os.path.join(destfolder, file)], check=True)
            except Exception as e:
                print(e)