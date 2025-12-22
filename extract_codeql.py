import os
import shutil
from pathlib import Path

def extract_codeql_components(repo_root, output_base):
    repo_path = Path(repo_root)
    output_path = Path(output_base)
    
    # Define targets and their sub-path logic
    # (Target Name, Sub-folder to look for, specific glob pattern)
    targets = [
        ("queries", "ql/src", "**/*.ql*"),
        ("tests", "ql/test", "**/*"),
        ("extractors", "extractor", "**/*")
    ]

    for label, sub_dir, pattern in targets:
        print(f"--- Extracting {label} ---")
        dest_folder = output_path / label
        dest_folder.mkdir(parents=True, exist_ok=True)

        # Search for the specific sub_dir within each language folder
        # e.g., java/ql/src, python/ql/src
        for lang_dir in repo_path.iterdir():
            if lang_dir.is_dir():
                source_path = lang_dir / sub_dir
                
                if source_path.exists():
                    # Create a language-specific subfolder in the destination
                    lang_dest = dest_folder / lang_dir.name
                    print(f"Copying {source_path} -> {lang_dest}")
                    
                    # Copy tree, ignoring errors like broken symlinks
                    shutil.copytree(source_path, lang_dest, dirs_exist_ok=True)

if __name__ == "__main__":
    # Update these paths to your local setup
    REPO_ROOT = "./codeql" 
    OUTPUT_DIR = "./codeql_extracted"
    
    extract_codeql_components(REPO_ROOT, OUTPUT_DIR)