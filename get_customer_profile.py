"""This is a use case, it defines interfaces for what IO it needs."""

import dependency_injection as di

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CustomerProfileRequest:
    """Use case input data."""
    id: int


@dataclass
class CustomerProfileResponse:
    """Use case output data."""
    first_name: str
    last_name: str
    age: int


@dataclass
class CustomerRegistryResponse:
    """Data format of the registry response."""
    first_name: str
    last_name: str
    age: int


@dataclass
class CustomerRegistryRequest:
    """Request for profile."""
    id: int


class CustomerProfileRegistry(ABC):
    """This is the use case's interface to the db."""

    @abstractmethod
    def get(self, request):
        """Get a profile by id. Must return CustomerRegistryResponse"""


class CustomerProfileRequester(ABC):
    """Input boundary of use case."""

    @abstractmethod
    def get(self, request):
        """Get profile by id."""


class GetCustomerProfileImpl(CustomerProfileRequester):
    """Use case implementation."""

    def __init__(self, registry):
        self.registry = registry

    def get(self, request):
        profile = self.registry.get(CustomerRegistryRequest(id=42))
        return CustomerProfileResponse(first_name=profile.first_name,
                                       last_name=profile.last_name,
                                       age=profile.age)
