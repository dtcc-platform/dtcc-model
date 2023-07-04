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
    def add_methods(cls, module, name=None):

        # hack needed create a class variable for each subclass
        if not hasattr(cls, "_methods"):
            cls._methods = []

        if isfunction(module):
            _add_method(cls, module, name)
        elif ismodule(module):
            for function_name, function in getmembers(module, isfunction):
                # print(fn_name)
                if not function_name.startswith("_"):
                    _add_method(cls, function, function_name)

    @classmethod
    def print_methods(cls, verbose=False):
        print(f"Methods for {cls.__name__}:")
        for name, parent_module, doc in cls._methods:
            print(f" - {name}: from {parent_module}")
            if verbose:
                print(f"   * {doc}")


def _add_method(cls, function, name=None):
    if name is None:
        name = function.__name__
    for idx, (function_name, _, _) in enumerate(cls._methods):
        if function_name == name:
            logging.warn(f"{function} Method {function_name} already exists, replacing it.")
            cls._methods.pop(idx)
            break
    cls._methods.append((name, function.__module__, function.__doc__))
    setattr(cls, name, function)
