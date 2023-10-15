#!/usr/bin/python3
"""
a class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    a class BaseModel that defines all common attributes/methods
    for other classes
    """
    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
            Instantiation of object
            Args:
                args:
                kwargs:
        """
        import models
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key,
                                datetime.strptime(value, BaseModel.format))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        A string representation that print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        import models
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
