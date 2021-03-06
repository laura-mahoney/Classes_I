"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""
        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5 

       
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)

    def get_total(self):
        return super(InternationalMelonOrder, self).get_total() + 3.0

    def set_country_code(self, country_code):
        self.set_country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """GovernmentMelonOrder"""
    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", 0.00)
    passed_inspection = False

    def mark_inspection(self, passed):

        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False

# """This file should have our order classes in it."""


# class DomesticMelonOrder(object):
#     """A domestic (in the US) melon order."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code