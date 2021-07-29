import pytest

from get_customer_profile import CustomerProfileRegistry, \
    CustomerRegistryResponse, CustomerProfileRequest, CustomerProfileResponse, \
    GetCustomerProfileImpl


class MockDb(CustomerProfileRegistry):
    """Sql database of customer profiles."""

    def get(self, request):
        """Should do some sql magic."""
        records = {
            '42': {'first_name': 'Jake', 'last_name': 'Waggoner', 'age': 42}
        }
        record = records[str(request.id)]
        return CustomerRegistryResponse(first_name=record['first_name'],
                                        last_name=record['last_name'],
                                        age=record['age'])


@pytest.fixture()
def profile_requester():
    """Return CustomerProfileRequester use case with mock db injected."""
    registry = MockDb()
    profile_requester = GetCustomerProfileImpl(registry)
    return profile_requester


def test_get_customer_profile_with_existing_profile(profile_requester):
    """Ensure existing profile is accessible."""
    request = CustomerProfileRequest(id=42)
    response = profile_requester.get(request)
    expected_response = CustomerProfileResponse(first_name='Jake',
                                                last_name='Waggoner',
                                                age=42)

    assert response == expected_response
