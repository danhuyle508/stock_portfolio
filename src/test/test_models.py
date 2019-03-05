from src.models import Company 

class TestClass():

    def test_create_company(self, session):
        company = Company(name='Google', symbol='goog')

        session.add(company)
        session.commit()

        assert city.id > 0

        company = Company.query.all()

        assert len(cities) == 1
        assert company[0].name == 'Google'
        assert company[0].symbol =='goog'