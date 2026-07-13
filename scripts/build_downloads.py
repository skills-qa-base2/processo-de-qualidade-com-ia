import os, zipfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

SOURCE_DIR = os.path.join(REPO_ROOT, "qa-skills-package")
DOWNLOADS_DIR = os.path.join(REPO_ROOT, "downloads")
ZIP_NAME = "qa-skills-package.zip"


def build_zip():
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    zip_path = os.path.join(DOWNLOADS_DIR, ZIP_NAME)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            dirs[:] = [d for d in dirs if d != ".git"]
            for name in files:
                full_path = os.path.join(root, name)
                # Archive name keeps the "qa-skills-package/" prefix so the zip
                # extracts into a self-named folder, matching the original package.
                rel_path = os.path.relpath(full_path, os.path.dirname(SOURCE_DIR))
                zf.write(full_path, rel_path)

    size_kb = os.path.getsize(zip_path) / 1024
    print(f"Built {zip_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    build_zip()
