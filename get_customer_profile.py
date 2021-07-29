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


class CustomerProfileRegistry(ABC):
    """This is the use case's interface to the db."""

    @abstractmethod
    def get_customer_profile(self, id):
        """Get a profile by id. Must return CustomerRegistryResponse"""


class GetCustomerProfile(ABC):
    """Use case: Get a customer's profile by id."""

    @abstractmethod
    def get_customer_profile(self, id):
        """Get profile by id."""


class GetCustomerProfileImpl(GetCustomerProfile):
    """Use case implementation."""

    def get_customer_profile(self, request):
        registry = di.inject('CustomerProfileRegistry')
        profile = registry.get_customer_profile(request.id)
        return CustomerProfileResponse(first_name=profile.first_name,
                                       last_name=profile.last_name,
                                       age=profile.age)
