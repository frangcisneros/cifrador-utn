import unittest
from flask import current_app
from app import create_app, db
from app.models import Texto, TextHistory


class TextTestCase(unittest.TestCase):
    """
    Test Texto and TextHistory models
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

    # Prueba la creación de un objeto Texto
    def test_texto_creation(self):
        text = Texto(content="Ejemplo de texto", length=100, language="Spanish")
        db.session.add(text)
        db.session.commit()
        self.assertIsNotNone(text.id)

    # Prueba la creación de un objeto TextHistory
    def test_text_history_creation(self):
        history = TextHistory(entries=["Entry 1", "Entry 2"])
        db.session.add(history)
        db.session.commit()
        self.assertIsNotNone(history.id)

    # Prueba la relación entre Texto y TextHistory
    def test_text_history_relation(self):
        text = Texto(content="Ejemplo de texto", length=100, language="Spanish")
        history = TextHistory(entries=["Entry 1", "Entry 2"])
        text.history = history
        db.session.add(text)
        db.session.commit()
        self.assertEqual(text.history_id, history.id)

    # Otros métodos de prueba pueden agregarse según sea necesario


if __name__ == "__main__":
    # Ejecuta el conjunto de pruebas si el script se ejecuta directamente
    unittest.main()
