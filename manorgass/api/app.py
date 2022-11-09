from flask import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(
        app.config['DB_URL'], encoding='utf-8', max_overflow=0)
    app.database = database

    return app


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


app = create_app()
app.json_encoder = CustomJSONEncoder


@app.route("/ping", methods=['GET'])
def ping():
    return "pong"


app.id_count = 1
app.users = {}


@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user = request.json
    new_user_id = app.database.execute(text("""
    INSERT INTO users(
        name,
        email,
        profile,
        hashed_password
    ) VALUES (
        :name,
        :email,
        :profile,
        :password
    )
    """), new_user).lastrowid

    row = current_app.database.execute(text("""
    SELECT id, name, email, profile FROM users WHERE id = :user_id
    """), {'user_id': new_user_id}).fetchone()

    created_user = {
        'id': row['id'],
        'name': row['name'],
        'email': row['email'],
        'profile': row['profile']
    } if row else None

    return jsonify(created_user)


app.tweets = []


@app.route('/tweet', methods=['POST'])
def tweet():
    payload = request.json
    user_id = int(payload['id'])
    tweet = payload['tweet']

    if user_id not in app.users:
        return '사용자가 존재하지 않습니다', 400

    if len(tweet) > 300:
        return '300자를 초과해습니다', 400

    # user_id = int(payload['id'])
    app.tweets.append({
        'user_id':   user_id,
        'tweet':   tweet
    })

    return '', 200


@app.route('/follow', methods=['POST'])
def follow():
    paylaod = request.json
    user_id = int(paylaod['id'])
    user_id_to_follow = int(paylaod['follow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return '사용자가 존재하지 않습니다', 400

    user = app.users[user_id]
    user.setdefault('follow', set()).add(user_id_to_follow)

    return jsonify(user)


@app.route('/unfollow', methods=['POST'])
def unfollow():
    paylaod = request.json
    user_id = int(paylaod['id'])
    user_id_to_follow = int(paylaod['unfollow'])

    if user_id not in app.users or user_id_to_follow not in app.users:
        return '사용자가 존재하지 않습니다', 400

    user = app.users[user_id]
    user.setdefault('follow', set()).discard(user_id_to_follow)

    return jsonify(user)


@app.route('/timeline/<int:user_id>', methods=['GET'])
def timeline(user_id):
    if user_id not in app.users:
        return '사용자가 존재하지 않습니다', 400

    follow_list = app.users[user_id].get('follow', set())
    follow_list.add(user_id)
    timeline = [tweet for tweet in app.tweets if tweet['user_id'] in follow_list]

    return jsonify({
        'user_id': user_id,
        'timeline': timeline
    })
