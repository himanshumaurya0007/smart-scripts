#!/usr/bin/env python3
"""
Folder Structure Creator

Features:
- Works on Windows, Linux, and macOS
- Creates folders relative to the current working directory
- Uses pathlib for cross-platform path handling
- Automatically creates missing parent directories
- Prevents errors when folders already exist
- Supports configurable folder hierarchies
- Provides creation statistics and status messages
- Handles permission and filesystem errors gracefully

Folder Structure:
- Creates a base folder defined by BASE_FOLDER
- Creates subject folders defined in FOLDER_STRUCTURE
- Creates module folders inside each subject folder
- Preserves existing folders using exist_ok=True

Example Output:

subjects
├── Machine-Learning
│   ├── module-1
│   ├── module-2
│   ├── module-3
│   ├── module-4
│   ├── module-5
│   └── module-6
├── Artificial-Intelligence
│   ├── module-1
│   ├── module-2
│   ├── module-3
│   ├── module-4
│   ├── module-5
│   └── module-6
└── Advanced-Artificial-Intelligence
    ├── module-1
    ├── module-2
    ├── module-3
    ├── module-4
    ├── module-5
    └── module-6
"""

from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_FOLDER = "subjects"

FOLDER_STRUCTURE = {
    "Machine-Learning": [
        "module-1",
        "module-2",
        "module-3",
        "module-4",
        "module-5",
        "module-6",
    ],
    "Artificial-Intelligence": [
        "module-1",
        "module-2",
        "module-3",
        "module-4",
        "module-5",
        "module-6",
    ],
    "Advanced-Artificial-Intelligence": [
        "module-1",
        "module-2",
        "module-3",
        "module-4",
        "module-5",
        "module-6",
    ],
}

# ============================================================================
# FOLDER CREATOR
# ============================================================================

def create_folder_structure():
    """
    Creates a predefined folder structure
    inside the current working directory.
    """

    root_directory = Path.cwd()

    base_path = root_directory / BASE_FOLDER

    folders_created = 0

    try:

        # ------------------------------------------------------------
        # CREATE BASE FOLDER
        # ------------------------------------------------------------

        base_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        # ------------------------------------------------------------
        # CREATE SUBFOLDERS
        # ------------------------------------------------------------

        for parent_folder, child_folders in FOLDER_STRUCTURE.items():

            parent_path = base_path / parent_folder

            parent_path.mkdir(
                parents=True,
                exist_ok=True,
            )

            folders_created += 1

            for child_folder in child_folders:

                child_path = parent_path / child_folder

                child_path.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                folders_created += 1

        # ------------------------------------------------------------
        # SUCCESS
        # ------------------------------------------------------------

        print("\nFolder structure created successfully.")
        print(f"Base Folder     : {base_path}")
        print(f"Folders Created : {folders_created}")

    except PermissionError as error:

        print("\nPermission denied.")
        print(error)

    except OSError as error:

        print("\nFailed to create folder structure.")
        print(error)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    create_folder_structure()