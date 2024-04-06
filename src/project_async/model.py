"""Module to define the data models from the API."""

from __future__ import annotations

import abc
import dataclasses
import typing

from dataclasses_json import DataClassJsonMixin, LetterCase, config, dataclass_json


@typing.dataclass_transform(kw_only_default=True)
class Model(DataClassJsonMixin, abc.ABC):

    def __init_subclass__(cls):
        cls = dataclasses.dataclass(frozen=True, kw_only=True)(cls)
        cls = dataclass_json(cls)
        return cls


class Response(Model):
    id: int
    foo_bar: str = dataclasses.field(
        metadata=config(letter_case=LetterCase.CAMEL)
    )
