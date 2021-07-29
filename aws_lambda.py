import dependency_injection as di

from get_customer_profile import CustomerProfileRequest


def lambda_handler(event, context):
    """Executes API call to get a customer profile."""

    request = CustomerProfileRequest(id=event['id'])
    # Lambda has no way to support this DI afaik
    profile_getter = di.inject('GetCustomerProfile')
    response = profile_getter.get_customer_profile(request)

    return {
        'profile': {
            'full_name': response.first_name + ' ' + response.last_name,
            'age': response.age
        }
    }
