#!/usr/bin/env python3
"""
Tree Structure Generator

Description:
- Generates a visual tree representation of the current working directory.
- Recursively scans all files and subdirectories.
- Exports the generated structure to a UTF-8 encoded text file.
- Produces output similar to the Unix `tree` command.
- Designed for project documentation, repository analysis, and AI context generation.

Features:
- Works on Windows, Linux, and macOS
- Uses pathlib for cross-platform filesystem operations
- Generates tree structure from the current working directory
- Recursively traverses nested directories
- Saves output to tree_structure.txt
- UTF-8 encoded output for full Unicode support
- Directories are displayed before files
- Case-insensitive sorting for consistent output
- Gracefully handles permission-restricted directories

Supports Excluding:
- Directory names
- File names
- Specific relative paths
- Wildcard patterns
    Examples:
        *.log
        *.pyc
        *.tmp
        *.cache

Default Exclusions:
- Generated output file
- Common dependency directories
- Build directories
- Cache directories
- Temporary files

Output Format Example:

my-project
├── .gitignore
├── README.md
├── frontend
│   ├── package.json
│   ├── public
│   └── src
│       ├── App.js
│       └── index.js
└── backend
    ├── app.js
    ├── server.js
    ├── controllers
    └── routes

Output File:
- tree_structure.txt

Typical Use Cases:
- Project documentation
- Repository auditing
- Project structure visualization
- Technical documentation generation
- AI-assisted code analysis
- Code review preparation
- System inventory reporting

Execution Behavior:
- Runs against the directory from which the script is executed.
- Does not depend on the script's location.
- Existing output files are overwritten.
- Excluded files and directories are omitted from traversal.

Platform Compatibility:
- Windows 10/11
- Linux distributions
- macOS

Author Notes:
- Uses only Python standard library modules.
- No third-party dependencies required.
"""

from pathlib import Path
import fnmatch

# ============================================================
# CONFIGURATION
# ============================================================

OUTPUT_FILE = "tree_structure.txt"

# Exclude directories by name anywhere in the tree
EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}

# Exclude files by name anywhere in the tree
EXCLUDE_FILES = {
    ".DS_Store",
    "Thumbs.db",
}

# Exclude specific relative paths
# Relative to the directory from which the script is executed.
#
# Examples:
# "frontend/dist"
# "backend/logs"
# "backend/.env"
#
EXCLUDE_PATHS = {
    "tree_structure.txt",  # prevent output file from appearing in tree
}

# Exclude wildcard patterns
EXCLUDE_PATTERNS = {
    "*.pyc",
    "*.log",
    "*.tmp",
}

# ============================================================
# HELPERS
# ============================================================

def matches_pattern(name: str) -> bool:
    """
    Check if a file or directory name matches
    any configured wildcard exclusion pattern.
    """
    return any(
        fnmatch.fnmatch(name, pattern)
        for pattern in EXCLUDE_PATTERNS
    )


def should_skip(path: Path, root: Path) -> bool:
    """
    Determine whether a file/folder should be excluded.
    """
    try:
        relative_path = path.relative_to(root).as_posix()
    except ValueError:
        return False

    # Exact relative path exclusion
    if relative_path in EXCLUDE_PATHS:
        return True

    # Directory exclusion
    if path.is_dir() and path.name in EXCLUDE_DIRS:
        return True

    # File exclusion
    if path.is_file() and path.name in EXCLUDE_FILES:
        return True

    # Wildcard exclusion
    if matches_pattern(path.name):
        return True

    return False


# ============================================================
# TREE GENERATION
# ============================================================

def generate_tree(directory: Path, root: Path, prefix: str = "") -> list[str]:
    """
    Recursively generate a tree structure.
    """
    lines = []

    try:
        entries = sorted(
            [
                entry
                for entry in directory.iterdir()
                if not should_skip(entry, root)
            ],
            key=lambda item: (
                not item.is_dir(),
                item.name.lower(),
            ),
        )
    except PermissionError:
        return [f"{prefix}└── [Permission Denied]"]

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1

        connector = "└── " if is_last else "├── "

        lines.append(
            f"{prefix}{connector}{entry.name}"
        )

        if entry.is_dir():
            child_prefix = (
                prefix + "    "
                if is_last
                else prefix + "│   "
            )

            lines.extend(
                generate_tree(
                    entry,
                    root,
                    child_prefix,
                )
            )

    return lines


# ============================================================
# OUTPUT
# ============================================================

def save_tree(root: Path, tree_lines: list[str]) -> Path:
    """
    Save generated tree to a UTF-8 text file.
    """
    output_path = root / OUTPUT_FILE

    content = [root.name]
    content.extend(tree_lines)

    output_path.write_text(
        "\n".join(content),
        encoding="utf-8",
    )

    return output_path


# ============================================================
# MAIN
# ============================================================

def main():
    root = Path.cwd()

    tree_lines = generate_tree(root, root)

    output_file = save_tree(root, tree_lines)

    print(f"Tree structure generated successfully.")
    print(f"Output file: {output_file}")


if __name__ == "__main__":
    main()