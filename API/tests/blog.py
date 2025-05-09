import unittest
from app import create_app, db
from app.models import Blog, UserAttribute
from app.config import TestConfig as config

class TestBlog(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config)
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            
            self.user = UserAttribute(
                id="test_id",
                name="test_name",
                value="test_value",
                user_id="test_user_id"
            )
            
            db.session.add(self.user)
            db.session.commit()
            
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            
            
            
if __name__ == '__main__':
    unittest.main()