from jinja2 import Environment, FileSystemLoader
import os

class MigrationGenerator:
    def __init__(self, class_name):
        self.class_name = class_name
        self.columns = []
        self.foreign_keys = []
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def add_column(self, column):
        self.columns.append(column)

    def add_foreign_key(self, foreign_key):
        self.foreign_keys.append(foreign_key)

    def generate_migration(self):
        template = self.env.get_template('/Templates/migration_template.sql.j2')

        migration_content = template.render(
            class_name=self.class_name,
            table_name=self.class_name.lower(),
            columns=self.columns,
            foreign_keys=self.foreign_keys
        )

        return migration_content
