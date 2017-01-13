"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    species = species
    qty = qty


    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(object):
    """A domestic (in the US) melon order."""
    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.shipped = False
        self.tax = 0.08


class InternationalMelonOrder(object):
    """An international (non-US) melon order."""
    order_type = "international"

    def __init__(selmark_shipped()f, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.shipped = False
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
