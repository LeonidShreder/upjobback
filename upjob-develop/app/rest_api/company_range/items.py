from core.company_range.company_range_api import get_ranges

__all__ = [
    'CompanyRangeList',
]


class BaseCompanyRange(object):
    """Represent base range company item.
    """
    def __init__(self, doc):
        self.id = str(doc.id)
        self.size_name = str(doc.size_name)
        self.size_value = str(doc.size_value)


class CompanyRangeList(BaseCompanyRange):

    def __init__(self, doc):
        super(CompanyRangeList, self).__init__(doc)

    @staticmethod
    def get_all_ranges():
        company_range_list = get_ranges()
        return [CompanyRangeList(c) for c in company_range_list]
