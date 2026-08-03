from pathlib import Path

ROOT = Path(".")

folders = [
    "config",
    "templates",
    "generators",
    "utils",
    "docs",
    "docs/architecture",
    "docs/guides",
    "docs/templates",
    "docs/examples",
    "examples",
    "tests",
    "tests/sample_outputs",
    "output",
    ".github",
    ".github/workflows",
    ".github/ISSUE_TEMPLATE"
]

files = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "requirements.txt",
    "bootstrap.py",
    "repository_template.json",

    "config/bootstrap.yaml",
    "config/repository_types.yaml",
    "config/workspace_mapping.yaml",

    "templates/README.md.j2",
    "templates/CHANGELOG.md.j2",
    "templates/ROADMAP.md.j2",
    "templates/CONTRIBUTING.md.j2",
    "templates/LICENSE.md.j2",
    "templates/repository.json.j2",
    "templates/CODEOWNERS.j2",
    "templates/SECURITY.md.j2",
    "templates/CODE_OF_CONDUCT.md.j2",

    "generators/__init__.py",
    "generators/directory_generator.py",
    "generators/file_generator.py",
    "generators/readme_generator.py",
    "generators/docs_generator.py",
    "generators/github_generator.py",
    "generators/vscode_generator.py",
    "generators/workspace_generator.py",
    "generators/metadata_generator.py",
    "generators/repository_generator.py",

    "utils/__init__.py",
    "utils/logger.py",
    "utils/filesystem.py",
    "utils/yaml_loader.py",
    "utils/validator.py",

    "tests/test_directory_generator.py",
    "tests/test_file_generator.py",
    "tests/test_repository_generator.py"
]

for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("✔ IAFE Repository Bootstrap structure created.")