from pathlib import Path
import os
import sys

# Run pip install with default arguments + options read from the app requirement
# installer args path.
# execv is simpler than subprocess, as it avoids needing to manage the subprocess
# or pipe in/out, which would add a lot of unnecessary complexity for no value.
# This script only helps build the command, it does not need to check the output at all.

os.execv(
    sys.executable,
    [
        sys.executable,
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
