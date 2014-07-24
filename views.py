
import flask
import models_redis as models
# import models_sql as models
from nanoblog import app


@app.route('/')
def index():
    posts = models.NanoblogPost.iter_all()
    return flask.render_template(
        'index.html',
        posts=posts
    )


@app.route('/create', methods=['GET', 'POST'])
def create():
    if flask.request.method == 'POST':
        print(flask.request.form.keys())
        post = models.NanoblogPost(
            title=flask.request.form['title'],
            body=flask.request.form['body'])
        post.addtodb()
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('create.html')
