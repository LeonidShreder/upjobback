from core.profession.profession_api import get_professions

__all__ = [
    'Profession',
]


class BaseProfession(object):
    """Represent base profession item.
    """
    def __init__(self, doc):
        self.id = str(doc.id)
        self.name = str(doc.name)
        self.value = str(doc.value)


class Profession(BaseProfession):

    def __init__(self, doc):
        super(Profession, self).__init__(doc)

    @staticmethod
    def get_all_professions():
        profession_list = get_professions()
        return [Profession(c) for c in profession_list]
