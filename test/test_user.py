import unittest
from flask import current_app
from app import create_app, db
from app.models import User, UserData


class UserTestCase(unittest.TestCase):
    """
    Test User model
    Necesitamos aplicar principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    YAGNI (You Aren't Gonna Need It) y SOLID (Single Responsibility Principle).
    """

    def setUp(self):
        # Crea una instancia de la aplicación Flask para pruebas
        self.app = create_app()
        # Crea un contexto de la aplicación y lo activa
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crea todas las tablas en la base de datos para las pruebas
        db.create_all()

    def tearDown(self):
        # Elimina la sesión de la base de datos y todas las tablas creadas
        db.session.remove()
        db.drop_all()
        # Desactiva y limpia el contexto de la aplicación
        self.app_context.pop()

    # Prueba si la aplicación Flask se crea correctamente
    def test_app(self):
        self.assertIsNotNone(current_app)

    # Prueba la creación de un usuario
    def test_user(self):
        # Crea un objeto UserData con información de prueba
        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        # Crea un objeto User y establece sus atributos
        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"

        # Verifica que los atributos del usuario se hayan establecido correctamente
        self.assertTrue(user.email, "test@test.com")
        self.assertTrue(user.username, "pabloprats")
        self.assertTrue(user.password, "Qvv3r7y")
        self.assertIsNotNone(user.data)
        self.assertTrue(user.data.address, "Address 1234")
        self.assertTrue(user.data.firstname, "Pablo")
        self.assertTrue(user.data.lastname, "Prats")
        self.assertTrue(user.data.phone, "54260123456789")

    def test_user_save(self):

        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"

        user.save()
        self.assertGreaterEqual(user.id, 1)
        self.assertTrue(user.email, "test@test.com")
        self.assertTrue(user.username, "pabloprats")
        self.assertTrue(user.password, "Qvv3r7y")
        self.assertIsNotNone(user.data)
        self.assertTrue(user.data.address, "Address 1234")
        self.assertTrue(user.data.firstname, "Pablo")
        self.assertTrue(user.data.lastname, "Prats")
        self.assertTrue(user.data.phone, "54260123456789")

    def test_user_delete(self):

        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"

        user.save()

        # borro el usuario
        user.delete()
        self.assertIsNone(User.find(user.id))

    def test_user_all(self):

        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"
        user.save()

        users = User.all()
        self.assertGreaterEqual(len(users), 1)

    def test_user_find(self):

        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"
        user.save()

        user_find = User.find(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id, user.id)
        self.assertEqual(user_find.email, user.email)


if __name__ == "__main__":
    # Ejecuta el conjunto de pruebas si el script se ejecuta directamente
    unittest.main()
