class ProductAlreadyInMonitorList(Exception):
    """Exception is raised when trying to add a product to monitor list
    that already is there."""

    pass


class ProductDoesNotExist(Exception):
    """Exception is raised when trying to get an object from database that does not exist"""

    pass
