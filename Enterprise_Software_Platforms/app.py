# Made By Pratik 
from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon

app = Flask(__name__)

# Initialize Mastodon instance
mastodon = Mastodon(
    access_token='5qBOiNYzUMKJMyc1SjTMC4i_6nYo96_v0jrRHpfZIkY',
    api_base_url='https://mastodon.social'  # Change to your Mastodon instance URL
)

@app.route('/', methods=['GET', 'POST'])
def index():
    post = None  # Initialize post to None
    if request.method == 'POST':
        action = request.form['action']
        status = request.form.get('status', '')

        if action == 'Post':
            # Create a new post
            post = mastodon.status_post(status)
            return redirect(url_for('index', post_id=post['id']))

        elif action == 'Retrieve':
            # Retrieve a post by ID
            post_id = request.form['post_id']
            try:
                post = mastodon.status(post_id)
            except Exception as e:
                return render_template('index.html', error=str(e))

        elif action == 'Delete':
            # Delete a post by ID
            post_id = request.form['post_id']
            try:
                mastodon.status_delete(post_id)
                return redirect(url_for('index', deleted=True))
            except Exception as e:
                return render_template('index.html', error=str(e))

    if request.args.get('post_id'):
        post_id = request.args.get('post_id')
        try:
            post = mastodon.status(post_id)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
