"""Load environment variables from a local .env file.

This intentionally uses only the standard library so the project does not need
an extra dependency such as python-dotenv.
"""

import os
from pathlib import Path


def load_env(path: Path) -> None:
    """Load KEY=VALUE pairs from *path* without overriding existing variables."""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key:
            os.environ.setdefault(key, value)
