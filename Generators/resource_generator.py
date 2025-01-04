from jinja2 import Environment, FileSystemLoader
import os
from .Elements.column import Column

class ResourceGenerator:
    def __init__(self, table_name, columns, sensitive_fields=None, relationships=None):
        self.table_name = table_name
        self.columns = columns
        self.class_name = table_name.capitalize()
        self.sensitive_fields = sensitive_fields if sensitive_fields else ['password']
        self.relationships = {rel['method_name']: rel['related_model'] for rel in relationships} if relationships else {}
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def generate_resource(self):
        fields = self._generate_fields()
        template = self.env.get_template('/Templates/resource_template.php.j2')

        return template.render(
            class_name=self.class_name,
            fields=fields
        )

    def generate_collection(self):
        template = self.env.get_template('/Templates/collection_template.php.j2')

        return template.render(
            class_name=self.class_name
        )

    def _generate_fields(self):
        fields = ""

        # Generate field mappings for columns, excluding sensitive fields
        for column in self.columns:
            if column.name not in self.sensitive_fields:
                fields += f"            '{column.name}' => $this->{column.name},\n"

        # Include timestamps if present
        fields += """            'created_at' => $this->created_at,
            'updated_at' => $this->updated_at,\n"""

        # Generate field mappings for relationships
        for relationship, resource_class in self.relationships.items():
            fields += f"            '{relationship}' => new {resource_class}($this->whenLoaded('{relationship}')),\n"

        return fields

