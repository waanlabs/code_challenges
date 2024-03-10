import subprocess


def autoflake():
    """
    Runs the autoflake tool to remove unused imports, expand star imports, ignore init module imports,
    remove duplicate keys, remove unused variables, and recursively process the 'code_challenges' directory.
    """
    subprocess.run(
        [
            "autoflake",
            "--in-place",
            "--remove-all-unused-imports",
            "--expand-star-imports",
            "--ignore-init-module-imports",
            "--remove-duplicate-keys",
            "--remove-unused-variables",
            "-r",
            "code_challenges",
        ]
    )


def isort():
    """
    Sorts the code challenges using the 'isort' tool.
    """
    subprocess.run(["isort", "code_challenges"])


def black():
    subprocess.run(["black", "."])


def flake():
    subprocess.run(["flake8", "."])


if __name__ == "__main__":
    autoflake()
