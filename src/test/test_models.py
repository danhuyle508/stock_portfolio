from src.models import Company, Portfolio 

class TestClass():

    def test_create_company(self, session):
        company = Company(name='Google', symbol='goog')

        session.add(company)
        session.commit()

        assert company.id > 0

        company = Company.query.all()

        assert len(company) == 1
        assert company[0].name == 'Google'
        assert company[0].symbol =='goog'

    def test_create_portfolios(self, session):
        user = User(name='cat')

        session.add(portfolio)
        session.commit()

        assert portfolio.id > 0

        portfolio = Portfolio.query.all()

        assert len(portfolio) == 1
        assert portfolio[0].name == 'cat'

    def test_create_portfolios(self, session):
        user = User(email='dog@gmail.com', password='123')

        session.add(user)
        session.commit()

        assert user.id > 0

        user = User.query.all()

        assert len(user) == 1
        assert user[0].email == 'dog@gmail.com'
        assert user[0].password == '123'            