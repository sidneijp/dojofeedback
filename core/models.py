from mongoengine import Document, StringField, ListField, EmbeddedDocumentField


class Comment(Document):
    description = StringField(max_length=100, required=True)


class Dojo(Document):
    name = StringField(max_length=100, required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

