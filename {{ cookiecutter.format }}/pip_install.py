from pathlib import Path
import os

# Run pip install with default arguments + options read from the app requirement
# installer args path

os.execv(
    "/app/bin/python3",
    [
        "/app/bin/python3",
        "-m",
        "pip",
        "install",
        "--no-cache-dir",
        "-r",
        "requirements.txt",
        "--target",
        "/app/briefcase/app_packages",
    ]
    + [
        arg
        for arg in (Path(__file__).parent / "pip-options.txt")
        .read_text()
        .split("\n")
        # skip empty lines, including trailing newlines or empty default file
        # (which contains a single newline character)
        if arg and not arg.isspace()
    ],
)
