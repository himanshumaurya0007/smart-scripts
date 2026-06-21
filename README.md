# Smart Scripts – Developer Utility Scripts Collection

A collection of cross-platform Python utilities designed to automate common development and project management tasks.

The repository contains reusable scripts for generating project structures, visualizing directory trees, consolidating project files, and accelerating project setup workflows.

All scripts are built using Python's standard library and are compatible with Windows, Linux, and macOS.

---

## 🧠 Features

- Cross-platform support (Windows, Linux, macOS)

- Zero third-party dependencies

- Tree structure generation

- Project structure scaffolding

- Folder structure creation

- Source code consolidation into a single file

- Configurable exclusion mechanisms

- UTF-8 compatible output

- Reusable and customizable configurations

- Suitable for documentation, AI context generation, and project automation

---

## 📁 Repository Structure

```bash
smart-scripts/
├── LICENSE
├── README.md
│
├── folder_structure_creator.py
├── project_structure_creator.py
└── tree_generator.py
```

---

## 🚀 Included Utilities

### 📂 Folder Structure Creator

Creates predefined folder hierarchies for educational, organizational, or project-management purposes.

#### Features

* Configurable folder structure
* Automatic parent creation
* Existing-folder safe
* Cross-platform path handling

#### Example Output

```text
subjects
├── Machine-Learning
│   ├── module-1
│   ├── module-2
│   └── module-3
├── Artificial-Intelligence
└── Advanced-Artificial-Intelligence
```

---

### 🏗️ Project Structure Creator

Creates complete project templates including folders and files.

#### Features

* Recursive structure generation
* File creation support
* Folder creation support
* Template file contents
* Customizable project blueprints

#### Example Output

```text
my-project
├── README.md
├── .gitignore
├── frontend
│   ├── src
│   └── public
└── backend
    ├── routes
    ├── controllers
    └── models
```

---

### 🌳 Tree Generator

Generates a visual tree representation of a directory and its subdirectories.

#### Features

* Recursive directory traversal
* UTF-8 tree formatting
* Exclude files
* Exclude directories
* Exclude relative paths
* Wildcard exclusion support
* Saves output to a text file

#### Example Output

```text
my-project
├── README.md
├── frontend
│   ├── package.json
│   └── src
└── backend
    ├── app.js
    └── server.js
```

#### Output File

```text
tree_structure.txt
```

---

## ⚙️ Requirements

### Software

| Requirement      | Version                 |
| ---------------- | ----------------------- |
| Python           | 3.10 or 3.10+           |
| Operating System | Windows / Linux / macOS |

### Dependencies

No external dependencies are required.

All scripts use only Python's standard library.

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/himanshumaurya0007/smart-scripts.git
cd smart-scripts
```

---

### 2. Run a Script

Example:

```bash
python folder_structure_creator.py
```

OR (for linux / macOS)

```bash
python3 folder_structure_creator.py
```

---

## 🛠️ Technologies Used

| Library                 | Purpose                              |
| ----------------------- | ------------------------------------ |
| pathlib                 | Cross-platform filesystem operations |
| os                      | Directory traversal                  |
| fnmatch                 | Wildcard pattern matching            |
| typing                  | Type annotations                     |
| Python Standard Library | Core functionality                   |

---

## 📱 Use Cases

### Documentation

Generate project tree structures for README files and technical documentation.

### AI Context Generation

Combine source files into a single document for AI-assisted code analysis.

### Project Bootstrapping

Create predefined folder and project structures instantly.

### Repository Auditing

Visualize and inspect repository organization.

### Educational Organization

Create subject-wise and module-wise directory hierarchies.

---

## 🔮 Future Enhancements

* JSON-based project templates
* YAML-based project templates
* Interactive CLI interface
* GUI desktop application

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Himanshu Maurya** — Full-Stack MERN Developer

📍 Badlapur, Mumbai, India

🏆 Winner – HackWave Hackathon 2024

📧 [himanshumaurya7781@gmail.com](mailto:himanshumaurya7781@gmail.com)

🔗 LinkedIn:
https://www.linkedin.com/in/himanshumaurya0007

🔗 GitHub:
https://github.com/himanshumaurya0007