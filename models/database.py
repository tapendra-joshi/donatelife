from extentions.extentions import db
import datetime
Column = db.Column
relationship = db.relationship

class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()


class IndexedTimestampModel(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods and created_at/last_updated_at indexed."""

    __abstract__ = True

    created_at = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.utcnow)
    last_updated_at = db.Column(db.DateTime, index=True, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Model(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True