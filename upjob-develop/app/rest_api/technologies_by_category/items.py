from core.technology.technology_api import get_technologies


class BaseFilter(object):
    def __init__(self, doc):
        self.category = doc['category']
        self.technology = doc['technologies']


class TechnologiesByCategory(BaseFilter):
    """Represent category item in list of filters.
    """

    def __init__(self, doc):
        super(TechnologiesByCategory, self).__init__(doc)

    @staticmethod
    def get_technologies_by_category(**args):
        technologies = get_technologies(**args)
        technologies_by_category = []
        for technology in technologies:
            if (technology.Category.category_value not in
                    [el['category'] for el in technologies_by_category]):
                technologies_by_category.append({
                    'category': technology.Category.category_value,
                    'technologies': [{
                        'id': technology.Technology.id,
                        'name': technology.Technology.name,
                    }],
                })
            else:
                for el in technologies_by_category:
                    if technology.Category.category_value == el['category']:
                        el['technologies'].append({
                            'id': technology.Technology.id,
                            'name': technology.Technology.name,
                        })
        return [TechnologiesByCategory(element) for element in
                technologies_by_category]
