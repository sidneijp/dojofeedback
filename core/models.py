from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField
from mongoengine.queryset import InvalidQueryError
from flask import abort


class Comment(EmbeddedDocument):
    description = StringField(max_length=100, required=True)
    status = StringField(max_length=100, required=True)


class Dojo(Document):
    name = StringField(max_length=100, required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

    def positives(self):
        positives = []
        for comment in self.comments:
            if comment.status == '1':
                positives.append(comment)
        return positives

    def negatives(self):
        negatives = []
        for comment in self.comments:
            if comment.status == '2':
                negatives.append(comment)

        return negatives

    @classmethod
    def get_or_404(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except (cls.MultipleObjectsReturned, cls.DoesNotExist, InvalidQueryError):
            abort(404)
