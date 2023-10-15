#!/usr/bin/python3
"""
a FileStorage class
"""
import json
import os
import models


class FileStorage:
    """
        A class that serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns:
                the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets into __objects the obj with key <obj class name>.id
                Args:
                    obj: object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing.
            If the file does not exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                if class_name in models.classNames:
                    obj = models.classNames[class_name](**value)
                    self.__objects[key] = obj
