from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import  SQLAlchemy


app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videoDb.db'
db= SQLAlchemy(app)

class VideoModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes= db.Column(db.Integer, nullable=False)

db.create_all()
#names={"chinmay": {"age": 29, "University": "Paderborn University"},
 #      "Aakash": {"age": 29, "Unoversity": "TU Berlin"}
 #      }
#class Hello(Resource):
  #  def get(self,name):
  #      return names[name]
    #def post(self):
      #  return {"data": "HI THIS IS REST API"}
video_put_args= reqparse.RequestParser()
video_put_args.add_argument("name",type=str, help="Name Of the Video is required", required=True)
video_put_args.add_argument("views",type=int, help="Views Of the Video is required", required=True)
video_put_args.add_argument("likes",type=int, help="Likes Of the Video is required", required=True)


video_update_args= reqparse.RequestParser()
video_update_args.add_argument("name",type=str, help="Name Of the Video is required")
video_update_args.add_argument("views",type=int, help="Views Of the Video is required")
video_update_args.add_argument("likes",type=int, help="Likes Of the Video is required")

video_delete_args= reqparse.RequestParser()
video_delete_args.add_argument("id",type=int, help="Name Of the Video is required")


resource_fileds= {'id': fields.Integer,
                  'name': fields.String,
                  'views': fields.Integer,
                  'likes': fields.Integer
                  }
#def videoID_not_present(video_id):
#    if video_id not in videos:
#        abort(404,message="Video ID not present...")
#def videoExist(video_id):
  #  if video_id in videos:
  #      abort(404, message="Video with ID is already pressent")

class Video(Resource):
    @marshal_with(resource_fileds)
    def get(self, video_id):
        result=VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video Is not found with given ID")
        return result
    @marshal_with(resource_fileds)
    def put(self, video_id):
        args= video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video Id Already Present")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    @marshal_with(resource_fileds)
    def patch(self, video_id):
        args=video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message="Video Does not Exist")
        if args['name']:
            result.name=args['name']
        if args['views']:
            result.views=args['views']
        if args['likes']:
            result.likes=args['likes']
        #db.session.add(result) if we have value already in database and we are updating it no need to add it again hence commented
        db.session.commit()
        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Delete is not possible because video Is not found with given ID")
        db.session.delete(result)
        db.session.commit()
        return result

api.add_resource(Video, "/video/<int:video_id>")


if __name__ == '__main__':
    app.run(debug=True)