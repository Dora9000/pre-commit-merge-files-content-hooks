import argparse
import sys


class Check:
    def _execute(self):
        return 0

    def execute(self):
        try:
            return self._execute()
        except Exception as e:
            sys.stderr.write(str(e) or f"Hook error happened: {repr(e)}")
            return 1


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    if not args.filenames:
        return 0

    return Check().execute()


if __name__ == "__main__":
    exit(main())
