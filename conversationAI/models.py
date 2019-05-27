__author__ = 'Mitu'

from datetime import datetime



from conversationAI import db , app



class Comment(db.Model):
    # Setup the relationship to the User table


    # Model for the Blog Posts on Website
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # Notice how we connect the BlogPost to a particular author
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    comment = db.Column(db.Text, nullable=False)

    toxicity = db.Column(db.Text, nullable=False)
    risk = db.Column(db.Text, nullable=False)

    def __unicode__(self):
        return self.id

    def __repr__(self):
        return "Post Id: {} --- Date: {} --- Title: {}".format(self.id,self.date,self.comment)

