# Made by Linh 
import unittest
from mastodon_service import create_post, retrieve_post, delete_post

class TestMastodonIntegration(unittest.TestCase):
    def test_create_post(self):
        response = create_post("Test post creation")
        self.assertIn('id', response)  # Ensure post has been created

    def test_retrieve_post(self):
        # Create a post first
        post = create_post("Test retrieve")
        retrieved_post = retrieve_post(post['id'])
        self.assertEqual(post['id'], retrieved_post['id'])  # Ensure post was retrieved correctly

    def test_delete_post(self):
        # Create a post first
        post = create_post("Test delete")
        delete_post(post['id'])
        # Add additional logic if necessary to check that the post has been deleted
