from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_cors import CORS
import datetime
from flask_marshmallow import Marshmallow



# DB connections
engine = create_engine('postgresql://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa')
connection = engine.connect()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://beobuojhegamsi:0d03035ef88099e1bd219b3772e17522354a9ac58068766ef6ac180fe38a83ec@ec2-52-3-130-181.compute-1.amazonaws.com:5432/d8gbvgrngr0fsa'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
metadata = MetaData()

# schemas!
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

# API Routes!
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

# beginning of template rendering page routes
@app.route("/")
def homepage():
    return render_template('home.html', )

@app.route("/articles")
def render_articles():
    return render_template('articles.html', articles = Articles.query.all() )

@app.route("/article/<string:id>")
def render_article(id):
    return render_template('article.html', articles = Articles.query.get(id))

# @app.route("/")
# def helloworld():
#     return {
#         'Hello':'World'
#     }

if __name__== '__main__':
    app.run(debug=True)
    # host = '127.0.0.1', port=3000, debug=True
    # 192.168.0.4:19000