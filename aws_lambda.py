from get_customer_profile import CustomerProfileRequest


class LambdaHandler:

    def __init__(self, profile_requester):
        self.profile_requester = profile_requester

    def lambda_handler(self, event, context):
        """Executes API call to get a customer profile."""

        request = CustomerProfileRequest(id=event['id'])
        response = self.profile_requester.get(request)

        return {
            'profile': {
                'full_name': response.first_name + ' ' + response.last_name,
                'age': response.age
            }
        }


def lambda_handler(event, context):
    handler = LambdaHandler()
    return handler.lambda_handler(event, context)
