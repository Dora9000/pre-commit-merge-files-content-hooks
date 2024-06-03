from pathlib import Path

import pytest

from pre_commit_merge_content_hooks.merge_files_content import Check


INPUT_FILES_DIR = Path(__file__).resolve(strict=True).parent.parent.parent / "feed_and_betting/db/models/clickhouse"
OUTPUT_FILE_DIR = Path(__file__).resolve(strict=True).parent


@pytest.mark.skip()
def test_single_file():
    for is_changed in (1, 0):
        output = Check(
            quiet=False,
            directory=str(INPUT_FILES_DIR),
            output_dir=str(OUTPUT_FILE_DIR),
            file_pattern='*.sql',
            output_filename='schema.sql',
        ).execute()

        assert output == is_changed

