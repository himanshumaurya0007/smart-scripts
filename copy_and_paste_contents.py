#!/usr/bin/env python3
"""
File Content Combiner

Features:
- Works on Windows, Linux, and macOS
- Scans the current working directory recursively
- Combines readable text files into a single output file
- Uses UTF-8 encoding throughout
- Reads files in chunks for memory efficiency
- Automatically skips:
    - The generated output file
    - The executing script
- Supports exclusion by:
    - Directory name
    - File name
    - Relative path
    - File extension
- Handles permission and decoding errors gracefully
- Provides processing statistics

Output:
- Generates a single file defined by OUTPUT_FILE
- Each file is separated by a visual separator
- Original relative file paths are preserved in headers

Example Output:

========================================================================================================================
FILE: backend/app.py
========================================================================================================================

<file contents>

========================================================================================================================
FILE: frontend/src/App.js
========================================================================================================================

<file contents>

Supported Exclusions:

Directories:
    .git
    node_modules
    dist
    build
    __pycache__
    .venv

Files:
    .env
    package-lock.json
    .DS_Store

Relative Paths:
    frontend/dist
    backend/logs

Extensions:
    .png
    .jpg
    .pdf
    .zip
    .mp4
    .woff2

Use Cases:
- Project documentation
- Code review preparation
- AI context generation
- Project archiving
- Source code consolidation
"""

from pathlib import Path
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

OUTPUT_FILE = "all_contents.txt"

SEPARATOR = "=" * 120

CHUNK_SIZE = 1024 * 1024  # 1 MB


# ----------------------------------------------------------------------------
# EXCLUDED DIRECTORIES
# ----------------------------------------------------------------------------

EXCLUDE_DIRECTORIES = {
    ".git",
    ".github",
    ".next",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "coverage",
}


# ----------------------------------------------------------------------------
# EXCLUDED FILES
# ----------------------------------------------------------------------------

EXCLUDE_FILES = {
    ".env",
    ".env.local",
    ".DS_Store",
    "Thumbs.db",
    "package-lock.json",
}


# ----------------------------------------------------------------------------
# EXCLUDED RELATIVE PATHS
# ----------------------------------------------------------------------------

EXCLUDE_PATHS = {
    "frontend/dist",
    "backend/logs",
    "frontend/src/config.js",
    "backend/logs/error.log",
}


# ----------------------------------------------------------------------------
# EXCLUDED EXTENSIONS
# ----------------------------------------------------------------------------

EXCLUDE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".webp",
    ".ico",

    ".pdf",

    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",

    ".exe",
    ".dll",
    ".so",
    ".dylib",

    ".bin",
    ".class",
    ".jar",

    ".pyc",
    ".pyo",

    ".mp3",
    ".mp4",
    ".wav",
    ".mov",

    ".ttf",
    ".woff",
    ".woff2",
}


# ============================================================================
# HELPERS
# ============================================================================

def normalize_path(path) -> str:
    """
    Convert any path into a normalized, lowercase POSIX path.

    Windows:
        frontend\\dist

    Linux/macOS:
        frontend/dist

    Both become:
        frontend/dist
    """

    return Path(path).as_posix().lower().strip("/")


def should_skip_directory(
    directory_path: Path,
    root_directory: Path,
) -> bool:
    """
    Check whether a directory should be skipped.
    """

    relative_path = normalize_path(
        directory_path.relative_to(root_directory)
    )

    return (
        directory_path.name.lower()
        in {name.lower() for name in EXCLUDE_DIRECTORIES}
        or relative_path
        in {path.lower() for path in EXCLUDE_PATHS}
    )


def should_skip_file(
    file_path: Path,
    root_directory: Path,
    output_path: Path,
) -> bool:
    """
    Check whether a file should be skipped.
    """

    try:
        if file_path.resolve() == output_path.resolve():
            return True
    except Exception:
        pass

    relative_path = normalize_path(
        file_path.relative_to(root_directory)
    )

    filename = file_path.name.lower()

    if filename in {name.lower() for name in EXCLUDE_FILES}:
        return True

    if relative_path in {
        path.lower()
        for path in EXCLUDE_PATHS
    }:
        return True

    if file_path.suffix.lower() in EXCLUDE_EXTENSIONS:
        return True

    return False


# ============================================================================
# FILE COMBINER
# ============================================================================

def combine_files():
    """
    Combine all readable files from the current directory and all
    subdirectories into a single output file.
    """

    root_directory = Path.cwd().resolve()

    output_path = root_directory / OUTPUT_FILE

    script_path = None

    try:
        script_path = Path(__file__).resolve()
    except NameError:
        pass

    files_processed = 0
    files_skipped = 0

    with open(
        output_path,
        mode="w",
        encoding="utf-8",
        newline="\n",
    ) as output_file:

        for current_root, dirs, files in os.walk(root_directory):

            current_directory = Path(current_root)

            # ------------------------------------------------------------
            # FILTER DIRECTORIES
            # ------------------------------------------------------------

            dirs[:] = [
                directory
                for directory in dirs
                if not should_skip_directory(
                    current_directory / directory,
                    root_directory,
                )
            ]

            # ------------------------------------------------------------
            # PROCESS FILES
            # ------------------------------------------------------------

            for filename in files:

                file_path = current_directory / filename

                try:

                    if (
                        script_path
                        and file_path.resolve() == script_path
                    ):
                        continue

                    if should_skip_file(
                        file_path,
                        root_directory,
                        output_path,
                    ):
                        continue

                    relative_path = file_path.relative_to(
                        root_directory
                    )

                    output_file.write(
                        f"\n{SEPARATOR}\n"
                    )

                    output_file.write(
                        f"FILE: {relative_path.as_posix()}\n"
                    )

                    output_file.write(
                        f"{SEPARATOR}\n\n"
                    )

                    with open(
                        file_path,
                        mode="r",
                        encoding="utf-8",
                        errors="ignore",
                    ) as source_file:

                        while True:

                            chunk = source_file.read(
                                CHUNK_SIZE
                            )

                            if not chunk:
                                break

                            output_file.write(chunk)

                    output_file.write("\n\n")

                    files_processed += 1

                except (
                    PermissionError,
                    UnicodeDecodeError,
                    OSError,
                ) as error:

                    files_skipped += 1

                    print(
                        f"Skipped: "
                        f"{file_path.relative_to(root_directory)}"
                    )

                    print(
                        f"Reason : {error}"
                    )

    print("\n" + SEPARATOR)

    print("Processing Complete")

    print(SEPARATOR)

    print(
        f"Files Processed : {files_processed}"
    )

    print(
        f"Files Skipped   : {files_skipped}"
    )

    print(
        f"Output File     : {output_path}"
    )


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    combine_files()