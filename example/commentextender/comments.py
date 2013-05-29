from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.discussion.browser.comments import CommentsViewlet as PloneAppDiscussionCommentsViewlet
from plone.app.discussion.browser.comments import CommentForm as PloneAppDiscussionCommentForm
from z3c.form import interfaces


class MyCommentForm(PloneAppDiscussionCommentForm):

    def updateWidgets(self):
        super(MyCommentForm, self).updateWidgets()
        self.widgets['author_name'].mode = interfaces.INPUT_MODE
        self.widgets['author_email'].mode = interfaces.INPUT_MODE


class CommentsViewlet(PloneAppDiscussionCommentsViewlet):

    form = MyCommentForm
    index = ViewPageTemplateFile('comments.pt')

    def get_commenter_home_url(self, username=None):
        if username is None:
            return None
        else:
            return "%s/memberhome/%s" % (self.context.portal_url(), username)
