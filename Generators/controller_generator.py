from jinja2 import Environment, FileSystemLoader
import os

class ControllerGenerator:
    def __init__(self, table_name):
        self.table_name = table_name
        self.class_name = table_name.capitalize()
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def generate(self):
        template = self.env.get_template('/Templates/controller_template.php.j2')

        return template.render(
            class_name=self.class_name,
            table_name=self.table_name
        )
