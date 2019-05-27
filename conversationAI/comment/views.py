__author__ = 'Mitu'


#blog_comment/views.py

from flask import render_template,url_for,flash, redirect,request,Blueprint,abort
from flask_login import current_user,login_required
from conversationAI import db
from conversationAI.models import Comment
from conversationAI.comment.forms import CommentPostForm
from wtforms.fields import FileField
from perspective import Perspective
from googletrans import Translator
from langdetect import detect


comment_posts = Blueprint('comment_posts',__name__)

allowed = ["TOXICITY",
           "SEVERE_TOXICITY",
           "TOXICITY_FAST",
           "ATTACK_ON_AUTHOR",
           "ATTACK_ON_COMMENTER",
           "INFLAMMATORY",
           "OBSCENE",
           ]

dictionary_toxicity = {"SEVERE_TOXICITY":"Severe toxicity",
           "TOXICITY_FAST" : "Fast toxicity",
           "ATTACK_ON_AUTHOR":"Attack on author",
           "ATTACK_ON_COMMENTER":"Attack on commenter",
           "INFLAMMATORY":"Inflammatory",
           "OBSCENE":"Obscene",
         }
pers = Perspective("AIzaSyDA41FbGVbRgcjnkzx_YjwoDa1qkxRpoA8")
translator = Translator()

@comment_posts.route('/create',methods=['GET','POST'])
def create_post():
    form = CommentPostForm()

    # print("user_id {} \n current_user_id {}".format(blog_posts.user_id,current_user.id))

    if form.validate_on_submit():


        temp_comment = form.comment.data
        if detect(temp_comment) != "en":
            try:
                temp_comment = translator.translate(temp_comment)
                temp_comment = temp_comment.text
            except:
                pass


        analyze_toxicity = pers.score(temp_comment, tests=[allowed[0],allowed[1],allowed[2],allowed[3],allowed[4],allowed[5],
                                                                  allowed[6]

                                                                  ])

        risk = ""
        countindex = 0;
        for key,value in dictionary_toxicity.items():
            countindex += 1;
            if analyze_toxicity[key].score >= 0.3:
                risk += value
                if countindex != 7:
                    risk +=" "



        toxicity = str(analyze_toxicity["TOXICITY"].score)

        comment = Comment(comment = form.comment.data,toxicity = toxicity,risk=risk)
        db.session.add(comment)
        db.session.commit()
        flash(" Comment Created")
        return redirect(url_for('core.index'))

    return render_template('submit.html',form=form)

