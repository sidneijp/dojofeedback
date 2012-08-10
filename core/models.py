from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField
from mongoengine.queryset import InvalidQueryError
from flask import abort


class Comment(EmbeddedDocument):
    description = StringField(max_length=500, required=True)
    status = StringField(max_length=100, required=True)


class Dojo(Document):
    name = StringField(max_length=100, required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

    def positives(self):
        return [comment for comment in self.comments if comment.status == '1']

    def negatives(self):
        return [comment for comment in self.comments if comment.status == '2']

    @classmethod
    def get_or_404(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except (cls.MultipleObjectsReturned, cls.DoesNotExist, InvalidQueryError):
            abort(404)
