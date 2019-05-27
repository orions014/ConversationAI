__author__ = 'Mitu'
from flask import render_template,request,Blueprint
from conversationAI.models import Comment
from conversationAI.comment.forms import CommentPostForm

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''


    page = request.args.get('page', 1, type=int)
    comment = Comment.query.order_by(Comment.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html',comment=comment)



# @core.route('/comment')
# def comment():
#     '''
#     This is the home page view. Notice how it uses pagination to show a limited
#     number of posts by limiting its query size and then calling paginate.
#     '''
#
#     form = CommentPostForm()
#
#     page = request.args.get('page', 1, type=int)
#     comment = Comment.query.order_by(Comment.date.desc()).paginate(page=page, per_page=5)
#     return render_template('submit.html',comment=comment,form=form)












