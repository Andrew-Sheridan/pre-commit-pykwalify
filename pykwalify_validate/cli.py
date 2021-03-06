import argparse, io, sys
from pathlib import Path
from typing import Dict
import yaml
from pykwalify.core import Core
from pykwalify.errors import SchemaError


def load_settings() -> Dict:
    settings = ".pykwalifyvalidate.yaml"
    path = Path(".") / settings

    if not path.exists():
        raise OSError(f"Cannot find {settings}")
    with path.open("r") as f:
        settings = yaml.safe_load(f)
    return settings


def main(argv=None):

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)
    filenames = args.filenames
    settings = load_settings()
    rules = settings["rules"]
    checked_files = set()
    errors = False
    for rule in rules:
        schema_file, data_dir = rule["schema_file"], rule["data_dir"]
        for filename in filenames:
            if filename not in checked_files:
                file_path = Path(filename)
                parent = file_path.parent
                if str(parent) == data_dir:
                    try:
                        print("\n" + filename)
                        file = Core(source_file=filename, schema_files=[schema_file])
                        file.validate(raise_exception=True)
                        checked_files.add(filename)
                    except SchemaError:
                        errors = True
                    else:
                        print("Validated")
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
