import datetime
from database import session
from models.company import Company
from models.profession import Profession
from models.user_profile_role import UserProfileRole
from models.category import Category
from models.company_range import CompanyRange
from models.userprofile import UserProfile
from models.purchase import Purchase
from models.employee import Employee
from models.vacancy import Vacancy
from models.competence import Competence
from models.requirement import Requirement
from models.technology import Technology
from models.experience import Experience

profession_list = list()
profession_list.append(Profession(name="Back End", value="backend"))
profession_list.append(Profession(name="Front End", value="frontend"))
profession_list.append(Profession(name="Project Manager", value="pm"))
profession_list.append(Profession(name="QA", value="qa"))
profession_list.append(Profession(name="Business Analyst", value="ba"))
profession_list.append(Profession(name="Dev Ops", value="dev_ops"))
profession_list.append(Profession(name="Mobile", value="mobile"))
profession_list.append(Profession(name="Designer", value="designer"))

role_list = list()
role_list.append(UserProfileRole(role_value='HR', role_name='hr'))
role_list.append(UserProfileRole(role_value='Lead', role_name='lead'))

category_list = list()
category_list.append(Category(category_name='programming_language',
                              category_value='Programming languages'))
category_list.append(Category(category_name='framework',
                              category_value='Framework'))
category_list.append(Category(category_name='tool',
                              category_value='Tool'))
category_list.append(Category(category_name='other',
                              category_value='Other'))
experience_list = list()
experience_list.append(Experience(experience_name='less_than_one',
                                  experience_value='less than 1 year'))
experience_list.append(
    Experience(experience_name='from_one_to_two', experience_value='1 - 2'))
experience_list.append(
    Experience(experience_name='from_two_to_three', experience_value='2 - 3'))
experience_list.append(
    Experience(experience_name='from_three_to_five', experience_value='3 - 5'))
experience_list.append(
    Experience(experience_name='from_five_to_ten', experience_value='5 - 10'))
experience_list.append(
    Experience(experience_name='more_than_ten', experience_value='10 +'))

company_range_list = list()
company_range_list.append(CompanyRange(size_name='zero', size_value='0'))
company_range_list.append(
    CompanyRange(size_name='from_1_to_20', size_value='1 - 20'))
company_range_list.append(
    CompanyRange(size_name='from_21_to_80', size_value='21 - 80'))
company_range_list.append(
    CompanyRange(size_name='from_81_to_200', size_value='81 - 200'))
company_range_list.append(
    CompanyRange(size_name='from_201_to_800', size_value='201 - 800'))
company_range_list.append(
    CompanyRange(size_name='more_than_800', size_value='800+'))

company_list = list()
company_list.append(
    Company(title='SoftServer', address='01015, вул. Лейпцизька 15',
            description='''SoftServe is the largest Ukrainian IT company, a 
            team of 5,500+ thinkers and makers, true professionals and good 
            people. We like what we do and do it well.''', size_range_id=4,
            phone_number='0670000000', email='softserver@gmail.com'))
company_list.append(
    Company(title='Ciklum', address='ул. Амосова, 12',
            description='''Сиклум (www.ciklum.com) — это международная 
            IT-компания, которая создает программное обеспечение и 
            предоставляет услуги и решения в различных сферах бизнеса и 
            технологий.''', size_range_id=4, phone_number='0680000000',
            email='ciklum@gmail.com'))
company_list.append(
    Company(title='Luxoft', address='бульвар И. Лепсе, 6-з',
            description='''Luxoft provides high-end business solutions 
            to clients across the globe. With deep domain expertise in the 
            finance, telecom, energy, automotive, travel and aviation 
            industries, the company consistently goes beyond its clients’ 
            expectations by bringing together technology, talent, 
            innovation, and the highest quality standards.''', size_range_id=5,
            phone_number='0560000000', email='luxoft@gmail.com'))

userprofile_list = list()
userprofile_list.append(
    UserProfile(email='andrew@gmail.com', password='123',
                full_name='Adrew Tonisov', phone_number='0670000000', role_id=1,
                company_id=1))
userprofile_list.append(
    UserProfile(email='maximus@gmail.com', password='123',
                full_name='Maxim Loten', phone_number='0680000000', role_id=2,
                company_id=1))
userprofile_list.append(
    UserProfile(email='alionas@gmail.com', password='123',
                full_name='Aliona Sorome', phone_number='0690000000', role_id=1,
                company_id=2))
userprofile_list.append(
    UserProfile(email='marisha@gmail.com', password='123',
                full_name='Marina Lonitova', phone_number='0560000000', role_id=2,
                company_id=3))

purchases_list = list()
purchases_list.append(
    Purchase(quantity=7, expiration_date=datetime.date.today(), sum=145,
             company_id=1))
purchases_list.append(
    Purchase(quantity=41, expiration_date=datetime.date.today(), sum=471,
             company_id=2))
purchases_list.append(
    Purchase(quantity=10, expiration_date=datetime.date.today(), sum=783,
             company_id=3))

employee_list = list()
employee_list.append(
    Employee(title='FullStack', full_name='Maxim Popov', user_id=1,
             public_id=14514, portfolio='I create some programs',
             is_activated=True, profession_id=1))
employee_list.append(
    Employee(title='FrontEnd', full_name='Aliona Virina', user_id=1,
             public_id=7545, portfolio='I create some programs',
             is_activated=False, profession_id=2))
employee_list.append(
    Employee(title='BackEnd', full_name='Albert Toherov', user_id=1,
             public_id=4158, portfolio='I create some programs',
             is_activated=False, profession_id=3))
employee_list.append(
    Employee(title='Mobile', full_name='Masha Sukarova', user_id=1,
             public_id=4132, portfolio='I create some programs',
             is_activated=True, profession_id=2))
employee_list.append(
    Employee(title='IOS', full_name='Alion Roherov', user_id=1,
             public_id=8652, portfolio='I create some programs',
             is_activated=True, profession_id=1))

vacancy_list = list()
vacancy_list.append(
    Vacancy(title='IOS', description='Some description', user_id=1,
            is_activated=True, price=1250, profession_id=4))
vacancy_list.append(
    Vacancy(title='Mobile', description='Some description', user_id=2,
            is_activated=True, price=1600, profession_id=3))
vacancy_list.append(
    Vacancy(title='FrontEnd', description='Some description', user_id=3,
            is_activated=True, price=1400, profession_id=1))
vacancy_list.append(
    Vacancy(title='IOS', description='Some description', user_id=4,
            is_activated=True, price=1050, profession_id=2))

competence_list = list()
competence_list.append(
    Competence(technology_id=1, employee_id=1, experience_id=2))
competence_list.append(
    Competence(technology_id=2, employee_id=4, experience_id=1))
competence_list.append(
    Competence(technology_id=3, employee_id=2, experience_id=4))
competence_list.append(
    Competence(technology_id=4, employee_id=3, experience_id=3))

requirement_list = list()
requirement_list.append(
    Requirement(technology_id=1, vacancy_id=1, experience_id=1))
requirement_list.append(
    Requirement(technology_id=4, vacancy_id=2, experience_id=4))
requirement_list.append(
    Requirement(technology_id=2, vacancy_id=3, experience_id=2))
requirement_list.append(
    Requirement(technology_id=3, vacancy_id=4, experience_id=3))

technology_list = list()
technology_list.append(Technology(name='html', category_id=1))
technology_list.append(Technology(name='python', category_id=1))
technology_list.append(Technology(name='js', category_id=1))
technology_list.append(Technology(name='flask', category_id=2))
technology_list.append(Technology(name='react', category_id=2))
technology_list.append(Technology(name='django', category_id=2))
technology_list.append(Technology(name='docker', category_id=3))

tables_list = [category_list, experience_list, company_range_list,
               profession_list, role_list, company_list, userprofile_list,
               purchases_list, employee_list, vacancy_list, technology_list,
               competence_list, requirement_list]

try:
    for table in tables_list:
        session.add_all(table)
        session.commit()
except Exception as e:
    session.rollback()
