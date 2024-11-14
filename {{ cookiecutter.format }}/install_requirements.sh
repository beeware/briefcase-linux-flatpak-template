#! /usr/bin/env sh

# Default pip-based installation. Briefcase may overwrite the contents of this file
# to configure requirement installation as required by the app configuration.
/app/bin/python3 -m pip install --no-cache-dir -r requirements.txt --target "$INSTALL_TARGET"
