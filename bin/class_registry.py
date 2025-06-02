# class_registry.py
from typing import Dict
from bin.class_base import Class, ClassType

class ClassRegistry:
    _registry: Dict[ClassType, Class] = {}

    @classmethod
    def register(cls, class_obj: Class):
        cls._registry[class_obj.name] = class_obj

    @classmethod
    def get(cls, class_type: ClassType) -> Class:
        if class_type not in cls._registry:
            print(f"[ERROR] Class '{class_type}' not in registry.")
            print("Available keys:", list(cls._registry.keys()))
            raise KeyError(class_type)
        return cls._registry[class_type]


    @classmethod
    def all(cls) -> Dict[ClassType, Class]:
        return cls._registry.copy()
    
    @classmethod
    def register_defaults(cls):
        """Load class definitions from JSON and register them."""
        from class_io import load_classes_from_file
        classes = load_classes_from_file()
        for c in classes:
            print(f"Registering class: {c.name} ({type(c.name)})")  # <-- Debug
            cls.register(c)
        
        print(f"Registered class keys: {list(cls._registry.keys())}")
