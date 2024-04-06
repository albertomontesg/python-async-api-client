"""Module to define the data models from the API."""

from __future__ import annotations

import abc
import dataclasses

from dataclasses_json import LetterCase, config, dataclass_json


class Model(abc.ABC):

    def __init_subclass__(cls):
        cls = dataclasses.dataclass(frozen=True, kw_only=True)(cls)
        cls = dataclass_json(cls)


class Response(Model):
    id: int
    foo_bar: str = dataclasses.field(
        metadata=config(letter_case=LetterCase.CAMEL)
    )
