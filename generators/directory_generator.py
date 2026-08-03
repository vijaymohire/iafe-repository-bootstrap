"""
===============================================================================
IAFE Repository Bootstrap
Directory Generator

Creates the standard directory structure for a new repository.

Author : Bhadale IT
Project: IAFE Repository Bootstrap
===============================================================================
"""

from pathlib import Path


class DirectoryGenerator:
    """
    Generates the standard directory structure for an IAFE repository.
    """
    VERSION = "1.0.0"

    STANDARD_DIRECTORIES = [

        # ------------------------------------------------------------------
        # GitHub
        # ------------------------------------------------------------------

        ".github",
        ".github/workflows",
        ".github/ISSUE_TEMPLATE",

        # ------------------------------------------------------------------
        # VS Code
        # ------------------------------------------------------------------

        ".vscode",

        # ------------------------------------------------------------------
        # Documentation
        # ------------------------------------------------------------------

        "docs",
        "docs/architecture",
        "docs/design",
        "docs/interfaces",
        "docs/api",
        "docs/deployment",
        "docs/governance",
        "docs/references",

        # ------------------------------------------------------------------
        # Source
        # ------------------------------------------------------------------

        "src",

        # ------------------------------------------------------------------
        # Tests
        # ------------------------------------------------------------------

        "tests",
        "tests/unit",
        "tests/integration",
        "tests/system",
        "tests/security",

        # ------------------------------------------------------------------
        # Examples
        # ------------------------------------------------------------------

        "examples",
        "samples",

        # ------------------------------------------------------------------
        # Assets
        # ------------------------------------------------------------------

        "assets",
        "scripts",

        # ------------------------------------------------------------------
        # Metadata
        # ------------------------------------------------------------------

        "iafe"

    ]

    def __init__(self):

        self.created = []

    def generate(self, repository_path):

        """
        Create directory structure.

        Parameters
        ----------
        repository_path : str | Path
        """

        repository_path = Path(repository_path)

        print()
        print("=" * 60)
        print("Creating Repository Directory Structure")
        print("=" * 60)

        for directory in self.STANDARD_DIRECTORIES:

            path = repository_path / directory

            path.mkdir(parents=True, exist_ok=True)

            self.created.append(path)

            print(f"✔ {directory}")

        print()
        print(f"Created {len(self.created)} directories.")

        return self.created