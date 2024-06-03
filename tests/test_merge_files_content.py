import os
import tempfile
import pytest

from pre_commit_merge_content_hooks.merge_files_content import Check


@pytest.fixture
def create_file(request, faker):
    def create(contents: list[str] | None = None):
        if not contents:
            contents = [faker.pystr(min_chars=1, max_chars=100) for _ in range(2)]

        content = "\n".join(contents)
        f = tempfile.NamedTemporaryFile(delete=False, mode="w")

        f.write(content)
        f.seek(0)

        def teardown():
            f.close()
            os.unlink(f.name)

        request.addfinalizer(teardown)
        return f

    yield create


@pytest.mark.skip()
def test_single_file(create_file, faker):
    contents = [faker.pystr(min_chars=1, max_chars=100) for _ in range(10)]

    file = create_file(contents)

    output = Check().execute()
    assert output == 0

