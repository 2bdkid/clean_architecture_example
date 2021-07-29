#!/usr/bin/env python3

import dependency_injection as di

from get_customer_profile import GetCustomerProfileImpl
from database import SqlDb
from aws_lambda import lambda_handler


def main():
    """Setup DI and simulate Lambda."""
    di.register('GetCustomerProfile', GetCustomerProfileImpl())
    di.register('CustomerProfileRegistry', SqlDb())

    # simulate Lambda call
    event = {
        'id': 42
    }

    response = lambda_handler(event, None)
    print(response)


if __name__ == '__main__':
    main()
