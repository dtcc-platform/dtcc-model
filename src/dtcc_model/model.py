from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar
from inspect import getmembers, isfunction, ismethod, ismodule
import logging
from google.protobuf.json_format import MessageToJson


@dataclass
class DTCCModel(ABC):
    """Base class for all DTCC models. Must implement to_proto and from_proto
    methods that converts to and from the protobuf representation.
    """

    @abstractmethod
    def to_proto(self):
        pass

    @abstractmethod
    def from_proto(self, pb):
        pass

    def to_json(self):
        return MessageToJson(self.to_proto(), including_default_value_fields=True)

    @classmethod
    def add_processors(cls, module, name=None):
        # print(f"called with args {cls} and {module} and {name}")

        # hack needed create a class variable for each subclass
        if not hasattr(cls, "_processors"):
            cls._processors = []

        if isfunction(module):
            _add_proc_fn(cls, module, name)
        elif ismodule(module):
            for fn_name, fn in getmembers(module, isfunction):
                # print(fn_name)
                if not fn_name.startswith("_"):
                    _add_proc_fn(cls, fn, fn_name)

    @classmethod
    def print_processors(cls, verbose=False):
        print(f"Processors for {cls.__name__}:")
        for name, parent_module, doc in cls._processors:
            print(f" - {name}: from {parent_module}")
            if verbose:
                print(f"   * {doc}")


def _add_proc_fn(cls, fn, name=None):
    # print(f"called with args {cls} and {fn} and {name}")
    if name is None:
        name = fn.__name__
    for idx, (fn_name, _, _) in enumerate(cls._processors):
        if fn_name == name:
            logging.warn(f"{fn} Processor {fn_name} already exists, replacing it.")
            cls._processors.pop(idx)
            break
    cls._processors.append((name, fn.__module__, fn.__doc__))
    setattr(cls, name, fn)
