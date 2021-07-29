#!/usr/bin/env python3

from get_customer_profile import GetCustomerProfileImpl
from database import SqlDb
from aws_lambda import LambdaHandler


def main():
    """Setup DI and simulate Lambda."""
    registry = SqlDb()
    profile_requester = GetCustomerProfileImpl(registry)

    # simulate Lambda call
    event = {
        'id': 42
    }

    l = LambdaHandler(profile_requester)
    response = l.lambda_handler(event, None)
    print(response)


if __name__ == '__main__':
    main()
