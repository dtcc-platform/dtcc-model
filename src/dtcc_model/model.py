from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar
from inspect import getmembers, isfunction, ismethod, ismodule
import logging


@dataclass
class DTCCModel(ABC):
    _processors: ClassVar[list] = []

    @abstractmethod
    def to_proto(self):
        pass

    @abstractmethod
    def from_proto(self, pb):
        pass

    @classmethod
    def add_processors(cls, module, name=None):
        if isfunction(module):
            if name is None:
                name = module.__name__
            cls._processors.append((name, module.__module__, module.__doc__))
            setattr(cls, name, module)
        elif ismodule(module):
            for fn_name, fn in getmembers(module, isfunction):
                # print(fn_name)
                if not fn_name.startswith("_"):
                    for idx, (name, _, _) in enumerate(cls._processors):
                        if name == fn_name:
                            logging.warn(
                                f"Processor {fn_name} already exists, replacing it."
                            )
                            cls._processors.pop(idx)
                            break
                    cls._processors.append((fn_name, {fn.__module__}, fn.__doc__))
                    setattr(cls, fn_name, fn)

    @classmethod
    def print_processors(cls, verbose=False):
        print(f"Processors for {cls.__name__}:")
        for name, parent_module, doc in cls._processors:
            print(f" - {name}: from {parent_module}")
            if verbose:
                print(f"   - {doc}")
