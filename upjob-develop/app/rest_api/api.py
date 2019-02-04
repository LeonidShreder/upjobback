from flask_restful import Api

from app import app
from rest_api.user_invite.resources import InviteUserResource
from rest_api.user_profile_role.resources import UserProfileRoleResource
from .company.resources import CompanyListResource, CompanyResource
from .userprofile.resources import UserProfileListResource, UserProfileResource
from .vacancy.resources import VacancyListResource, VacancyResource
from .profession.resources import ProfessionResource
from .employee.resources import EmployeeListResource, EmployeeResource
from .quantity.resources import QuantityResource
from .company_range.resources import CompanyRangeResource
from .technologies_by_category.resources import TechnologiesByCategoryRecource

api = Api(app)

api.add_resource(CompanyListResource, '/companies')
api.add_resource(CompanyResource, '/companies/<company_id>')
api.add_resource(UserProfileListResource, '/userprofiles')
api.add_resource(UserProfileResource, '/userprofiles/<user_profile_id>')
api.add_resource(VacancyListResource, '/vacancies')
api.add_resource(EmployeeListResource, '/employees')
api.add_resource(EmployeeResource, '/employee')
api.add_resource(VacancyResource, '/vacancy')
api.add_resource(TechnologiesByCategoryRecource, '/technologies_by_category')
api.add_resource(ProfessionResource, '/professions')
api.add_resource(CompanyRangeResource, '/ranges')
api.add_resource(UserProfileRoleResource, '/roles')
api.add_resource(InviteUserResource, '/invite_user')
api.add_resource(QuantityResource, '/quantity/<company_id>')
