from core.vacancy.vacancy_api import (
    get_vacancies,
    get_vacancy_by_id,
    get_vacancy_info_map,
    update_vacancy_by_id,
)

__all__ = [
    'VacancyCard',
    'VacancyInList',
]


class BaseCompany(object):
    def __init__(self, doc, vacancy_info_map):
        try:
            doc = doc.Vacancy
        except AttributeError:
            doc = doc
        self.id = str(doc.id)
        self.title = doc.title
        self.description = doc.description
        self.user_id = doc.user_id
        self.is_activated = doc.is_activated
        self.price = doc.price
        vacancy_fields = vacancy_info_map.get(self.id)
        if vacancy_fields is not None:
            self.company = vacancy_fields.get('company')
            self.profession = vacancy_fields.get('profession')
            self.requirements = []
            for requirement in vacancy_fields.get('requirement'):
                self.requirements.append({'id': requirement.get('id'),
                                          'name': requirement.get('name'),
                                          'experience':
                                              requirement.get('experience'),
                                          })


class VacancyInList(BaseCompany):
    """Represent vacancy item in list.
    """

    def __init__(self, doc, vacancy_info_map):
        super(VacancyInList, self).__init__(doc, vacancy_info_map)

    @staticmethod
    def get_vacancy_items(args):
        vacancy_list = get_vacancies(args)
        vacancy_info_map = get_vacancy_info_map(vacancy_list)
        return [VacancyInList(vacancy, vacancy_info_map) for vacancy in
                vacancy_list]


class VacancyCard(BaseCompany):
    """Represent vacancy card.
    """

    def __init__(self, doc, vacancy_info_map):
        super().__init__(doc, vacancy_info_map)

    @staticmethod
    def get_vacancy(args):
        vacancy = get_vacancy_by_id(args)
        vacancy_info_map = get_vacancy_info_map(vacancy)
        return VacancyCard(vacancy, vacancy_info_map)

    @staticmethod
    def put_vacancy(args):
        update_vacancy_by_id(args)
        vacancy = get_vacancy_by_id(args)
        vacancy_info_map = get_vacancy_info_map(vacancy)
        return VacancyCard(vacancy, vacancy_info_map)
