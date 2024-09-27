import unittest
from app import app, db
from app.models import Task


class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test app and database for testing
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Tear down and clean up after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        # Test the index route
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Gerenciador de Tarefas", response.data)

    def test_create_task(self):
        # Test the task creation route
        response = self.client.post(
            "/create",
            data=dict(title="Teste de Tarefa", description="Descrição de teste"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Teste de Tarefa", response.data)

    def test_update_task(self):
        # Test the task update functionality
        with app.app_context():
            task = Task(title="Tarefa Original", description="Descrição original")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/update/{task_id}",
            data=dict(title="Tarefa Atualizada", description="Descrição atualizada"),
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tarefa Atualizada", response.data)

    def test_delete_task(self):
        # Test the task deletion functionality
        with app.app_context():
            task = Task(title="Tarefa para Deletar", description="Será deletada")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.get(f"/delete/{task_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Tarefa para Deletar", response.data)


if __name__ == "__main__":
    unittest.main()
