from core.quantity.quantity_api import get_quantity

__all__ = [
    'Quantity',
]


class BaseQuantity(object):
    """Represent base item for amount of available slots in quantity.
    """
    def __init__(self,  doc):
        self.quantity = doc.quantity


class Quantity(BaseQuantity):

    def __init__(self, doc):
        super(Quantity, self).__init__(doc)

    @staticmethod
    def get_quantity_by_company_id(company_id):
        quantity = get_quantity(company_id)
        return Quantity(quantity)
