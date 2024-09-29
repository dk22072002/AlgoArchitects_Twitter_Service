# Done by Dhruv
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, MastodonUnauthorizedError
import time

# Set up Mastodon instance with the access token and API URL
mastodon = Mastodon(
    access_token='5qBOiNYzUMKJMyc1SjTMC4i_6nYo96_v0jrRHpfZIkY',
    api_base_url='https://mastodon.social'
)

# Function to handle post creation
def create_post(status):
    try:
        # Validate input
        if not status or len(status.strip()) == 0:
            raise ValueError("Status cannot be empty")

        # Create post
        post = mastodon.status_post(status)
        return post
    except ValueError as ve:
        print(f"Input error: {ve}")
        return None
    except MastodonRatelimitError:
        print("Rate limit reached. Please wait and try again later.")
        return None
    except MastodonUnauthorizedError:
        print("Authentication error: Please check your access token.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to handle post retrieval
def retrieve_post(post_id):
    try:
        # Retrieve post
        post = mastodon.status(post_id)
        return post
    except MastodonNotFoundError:
        print(f"Post with ID {post_id} not found.")
        return None
    except MastodonRatelimitError:
        print("Rate limit reached. Please wait and try again later.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to handle post deletion
def delete_post(post_id):
    try:
        # Delete post
        mastodon.status_delete(post_id)
        print(f"Post with ID {post_id} deleted successfully.")
    except MastodonNotFoundError:
        print(f"Post with ID {post_id} not found.")
    except MastodonRatelimitError:
        print("Rate limit reached. Please wait and try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == '__main__':
    # Create a post
    post = create_post('Hello, Mastodon with error handling!')
    if post:
        print("Created Post:", post)

    # Retrieve the post
    if post:
        retrieved_post = retrieve_post(post['id'])
        if retrieved_post:
            print("Retrieved Post:", retrieved_post)

    # Delete the post
    if post:
        delete_post(post['id'])
