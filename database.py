from get_customer_profile import CustomerProfileRegistry, \
    CustomerRegistryResponse


class SqlDb(CustomerProfileRegistry):
    """Sql database of customer profiles."""

    def get(self, request):
        """Should do some sql magic."""
        record = {'first_name': 'Jake', 'last_name': 'Waggoner', 'age': 42}
        return CustomerRegistryResponse(first_name=record['first_name'],
                                        last_name=record['last_name'],
                                        age=record['age'])
