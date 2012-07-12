from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField


class Comment(EmbeddedDocument):
    description = StringField(max_length=100, required=True)


class Dojo(Document):
    name = StringField(max_length=100, required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

