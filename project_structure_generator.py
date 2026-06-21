#!/usr/bin/env python3
"""
Project Structure Creator

Features:
- Works on Windows, Linux, and macOS
- Creates complete project structures
- Supports folders and files
- Uses pathlib for cross-platform compatibility
- Creates structures relative to the current working directory
- Automatically creates parent directories
- Supports nested folder hierarchies
- Prevents overwriting existing files
- Supports template file content
- Handles filesystem and permission errors gracefully

Capabilities:
- Create folders
- Create files
- Pre-populate files with starter content
- Generate reusable project templates

Example Structure:

my-project
├── .gitignore
├── README.md
├── LICENSE
├── frontend
│   ├── .env
│   ├── package.json
│   ├── public
│   │   └── index.html
│   └── src
│       ├── App.js
│       ├── components
│       ├── pages
│       ├── services
│       └── utils
└── backend
    ├── .env
    ├── app.js
    ├── server.js
    ├── config
    │   └── db.js
    ├── controllers
    ├── middlewares
    ├── models
    └── routes

Use Cases:
- MERN applications
- Python projects
- Java applications
- Documentation templates
- Course structures
- Custom project scaffolding
"""

from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

PROJECT_NAME = "my-project"

PROJECT_STRUCTURE = {
    ".gitignore": "",
    "README.md": "# My Project\n",
    "LICENSE": "",

    "frontend": {
        ".env": "",
        "package.json": "",
        "src": {
            "App.js": "",
            "index.js": "",
            "components": {},
            "pages": {},
            "services": {},
            "utils": {},
        },
        "public": {
            "index.html": "",
        },
    },

    "backend": {
        ".env": "",

        "config": {
            "db.js": "",
        },

        "controllers": {},

        "middlewares": {
            "error.middleware.js": "",
        },

        "models": {},

        "routes": {},

        "data": {
            "seed.js": "",
        },

        "app.js": "",
        "server.js": "",
    },
}

# ============================================================================
# CREATION ENGINE
# ============================================================================

def create_structure(
    base_path: Path,
    structure: dict,
):
    """
    Recursively create folders and files.
    """

    for name, content in structure.items():

        current_path = base_path / name

        # ------------------------------------------------------------
        # DIRECTORY
        # ------------------------------------------------------------

        if isinstance(content, dict):

            current_path.mkdir(
                parents=True,
                exist_ok=True,
            )

            create_structure(
                current_path,
                content,
            )

        # ------------------------------------------------------------
        # FILE
        # ------------------------------------------------------------

        else:

            current_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            if not current_path.exists():

                current_path.write_text(
                    str(content),
                    encoding="utf-8",
                )


# ============================================================================
# MAIN
# ============================================================================

def create_project_structure():

    root_directory = Path.cwd()

    project_path = (
        root_directory
        / PROJECT_NAME
    )

    try:

        project_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        create_structure(
            project_path,
            PROJECT_STRUCTURE,
        )

        print(
            "\nProject structure created successfully."
        )

        print(
            f"Location: {project_path}"
        )

    except PermissionError as error:

        print(
            "\nPermission denied."
        )

        print(error)

    except OSError as error:

        print(
            "\nFailed to create project structure."
        )

        print(error)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    create_project_structure()