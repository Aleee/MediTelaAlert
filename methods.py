from PyQt5.QtWidgets import *
from typing import Any


def str_to_int(text: str):
    try:
        return int(text)
    except (ValueError, TypeError):
        return None


def get_custom_property(widget: QWidget) -> (str, Any):
    if widget.property("property"):
        return widget.property("property"), widget.property("value")
    else:
        return "EMPTY", 0
