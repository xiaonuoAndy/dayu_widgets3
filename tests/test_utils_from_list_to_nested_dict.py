# -*- coding: utf-8 -*-
"""
Test the function from_list_to_nested_dict.
"""

# Import third-party modules
import pytest

# Import local modules
from dayu_widgets import utils


TEST_DATA = (
    (
        ["a/b/c"],
        [
            {
                "value": "a",
                "label": "a",
                "children": [
                    {
                        "value": "b",
                        "label": "b",
                        "children": [{"value": "c", "label": "c"}],
                    }
                ],
            }
        ],
    ),
    (
        ["a/b"],
        [{"value": "a", "label": "a", "children": [{"value": "b", "label": "b"}]}],
    ),
    (
        ["/a/b"],
        [{"value": "a", "label": "a", "children": [{"value": "b", "label": "b"}]}],
    ),
    (
        ["a/b/"],
        [{"value": "a", "label": "a", "children": [{"value": "b", "label": "b"}]}],
    ),
    (
        ["a/b/c", "a/b/d"],
        [
            {
                "value": "a",
                "label": "a",
                "children": [
                    {
                        "value": "b",
                        "label": "b",
                        "children": [
                            {"value": "c", "label": "c"},
                            {"value": "d", "label": "d"},
                        ],
                    }
                ],
            }
        ],
    ),
    (
        ["a/b/c", "a/m/n"],
        [
            {
                "value": "a",
                "label": "a",
                "children": [
                    {
                        "value": "b",
                        "label": "b",
                        "children": [{"value": "c", "label": "c"}],
                    },
                    {
                        "value": "m",
                        "label": "m",
                        "children": [{"value": "n", "label": "n"}],
                    },
                ],
            }
        ],
    ),
    (
        ["中国/北京/故宫", "中国/苏州/狮子林"],
        [
            {
                "value": "中国",
                "label": "中国",
                "children": [
                    {
                        "value": "北京",
                        "label": "北京",
                        "children": [{"value": "故宫", "label": "故宫"}],
                    },
                    {
                        "value": "苏州",
                        "label": "苏州",
                        "children": [{"value": "狮子林", "label": "狮子林"}],
                    },
                ],
            }
        ],
    ),
)


@pytest.mark.parametrize("input_,result", TEST_DATA, ids=[str(i[0]) for i in TEST_DATA])
def test_from_list_to_nested_dict(input_, result):
    """Test with different level string."""
    assert utils.from_list_to_nested_dict(input_) == result


def test_with_sep():
    """Test when sep is given."""
    result = [
        {
            "value": "a",
            "label": "a",
            "children": [
                {
                    "value": "b",
                    "label": "b",
                    "children": [
                        {"value": "c", "label": "c"},
                        {"value": "d", "label": "d"},
                    ],
                }
            ],
        }
    ]
    assert utils.from_list_to_nested_dict(["a@b@c", "a@b@d"], sep="@") == result


@pytest.mark.parametrize(
    "input_arg, error_type",
    (
        (3, int),
        ("a_string", str),
        ({}, dict),
        (object(), object),
    ),
)
def test_with_input_wrong_type(input_arg, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        utils.from_list_to_nested_dict(input_arg)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'input' should be list or tuple or set, " "but get {}".format(error_type)


@pytest.mark.parametrize(
    "input_sep, error_type",
    (
        (3, int),
        ([], list),
        ((1,), tuple),
        (set(), set),
        ({}, dict),
        (object(), object),
    ),
)
def test_with_sep_wrong_type(input_sep, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        utils.from_list_to_nested_dict(["a@b@c", "a@b@d"], input_sep)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'sep' should be str, " "but get {}".format(error_type)
