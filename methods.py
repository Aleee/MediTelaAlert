from PyQt5.QtWidgets import *
from typing import Any, Union
import consts


def str_to_int(text: Union[str, int]):
    try:
        return int(text)
    except (ValueError, TypeError):
        return None


def get_custom_property(widget: QWidget) -> (str, Any):
    if widget.property("property"):
        return widget.property("property"), widget.property("value")
    else:
        return "EMPTY", 0


def get_column_number_from_name(name: str) -> int:
    for key, value in consts.TV_HEADERS.items():
        if value[3] == name:
            return key


def get_number_of_init_columns() -> int:
    return get_column_number_from_name(consts.REF_COLUMNS["lab_start"])


def get_number_of_lab_columns() -> int:
    return get_column_number_from_name(consts.REF_COLUMNS["instr_start"]) - get_number_of_init_columns()


def get_number_of_instr_columns() -> int:
    return get_column_number_from_name(consts.REF_COLUMNS["instr_end"]) - get_column_number_from_name(consts.REF_COLUMNS["instr_start"]) + 1
