from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar
from inspect import getmembers, isfunction, ismethod, ismodule
import logging
from google.protobuf.json_format import MessageToJson
from copy import deepcopy


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

    def to_json(self) -> str:
        """Return a JSON representation of the object.

        Returns
        -------
            str
                A JSON string representing the object.
        """
        return MessageToJson(self.to_proto(), including_default_value_fields=True)

    def copy(self):
        """Return a copy of the object.

        Returns
        -------
            DTCCModel: A copy of the object.
        """
        return deepcopy(self)

    @classmethod
    def add_methods(cls, module, name=None):
        """Adds methods from a module or function to the class.

        Parameters
        ----------
            module: module or function
                A function or module containing the methods to add.
            name : str
                The name of the method to add, if None use the
                function/method name (default None).

        Raises
        ------
            TypeError
             If module parameter is not a module or function.

        Returns
        -------
            None
        """
        # hack needed create a class variable for each subclass
        if not hasattr(cls, "_methods"):
            cls._methods = []

        if isfunction(module):
            if name is None:
                name = module.__name__
            _add_method(cls, module, name)
        elif ismodule(module):
            for function_name, function in getmembers(module, isfunction):
                if not function_name.startswith("_"):
                    _add_method(cls, function, function_name)
        else:
            raise TypeError("Expected a module or function")

    @classmethod
    def print_methods(cls, verbose=False):
        """
        Print the methods that have been added to the class.

        Parameters
        ----------
        verbose : bool, optional
            Whether to print the docstring of each method (default False).

        Returns
        -------
        None
        """
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
            logging.warn(
                f"{function} Method {function_name} already exists, replacing it."
            )
            cls._methods.pop(idx)
            break
    cls._methods.append((name, function.__module__, function.__doc__))
    setattr(cls, name, function)
