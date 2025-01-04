from jinja2 import Environment, FileSystemLoader
import os

class ModelGenerator:
    def __init__(self, table_name, columns, relationships):
        self.table_name = table_name
        self.columns = columns
        self.protected_columns = ['password', 'token', 'code']
        self.relationships = relationships
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def add_relationship(self, method_name, relationship_type, related_model):
        """Add a relationship method to the model."""
        self.relationships.append({
            "method_name": method_name,
            "relationship_type": relationship_type,
            "related_model": related_model
        })

    def generate_model(self):
        class_name = ''.join(word.capitalize() for word in self.table_name.split('_'))
        fillable_columns = [col.name for col in self.columns if col.name not in self.protected_columns]
        guarded_columns = [col.name for col in self.columns if col.name in self.protected_columns]

        template = self.env.get_template('/Templates/model_template.php.j2')

        model_content = template.render(
            class_name=class_name,
            table_name=self.table_name,
            fillable_columns=fillable_columns,
            guarded_columns=guarded_columns,
            relationships=self.relationships
        )

        return model_content
