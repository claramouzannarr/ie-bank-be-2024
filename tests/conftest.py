import pytest
from iebank_api.models import Account
from iebank_api import db, app



@pytest.fixture
def testing_client(scope='module'):
    with app.app_context():
        db.create_all()
<<<<<<< HEAD
        account = Account('Test Account', '€', 'Lebanon')
=======
        account = Account('Test Account', 'Lebanon', '€')
>>>>>>> 86c5945c58957430bac44d413d69e5d05cfff7ae
        db.session.add(account)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()