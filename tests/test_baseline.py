import pytest

from baseline import tasks


@pytest.mark.req("BASELINE-04")
def test_first_missing():
    required = ["item_1", "item_2", "item_3"]
    present = ["item_1", "item_3"]
    assert tasks.first_missing(required, present) == "item_2"