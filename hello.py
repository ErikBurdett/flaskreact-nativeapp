from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine
from flask_migrate import Migrate
import datetime
from flask_marshmallow import Marshmallow
# import psycopg2
# import urllib.parse
# import os

# db stuff
# result = urlsparse("postgres://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa")
# urllib.parse.uses_netloc.append("postgres://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa")
# postgres_url = urllib.parse.urlparse(os.environ.get("postgres://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa"))
engine = create_engine('postgresql://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa')
connection = engine.connect()
# conn = psycopg2.connect(
#   database=postgres_url.path[1:],
#   user=postgres_url.username,
#   password=postgres_url.password,
#   host=postgres_url.hostname,
#   port=postgres_url.port
#   )
# conn.autocommit = True



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
metadata = MetaData()

# articlestable = Table('articles', metadata, autoload=True, autoload_with=engine)
# print(repr(articlestable))

class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    def __init__(self, title,body):
        self.title = title
        self.body = body
    def __repr__(self):
        return f"<Articles {self.name}>"

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date' )

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@app.route("/get", methods = ['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@app.route("/get/<id>/", methods = ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

@app.route("/update/<id>/", methods = ['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)

@app.route("/delete/<id>/", methods = ['DELETE'])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)

@app.route("/add", methods = ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


@app.route("/homepage")
def homepage():
    return "Hello Universe. Hello, Heroku. Howdy."

@app.route("/")
def helloworld():
    return {
        'Hello':'World'
    }

if __name__== '__main__':
    app.run(debug=True)
    # host = '127.0.0.1', port=3000, debug=True
    # 192.168.0.4:19000