from jinja2 import Environment, FileSystemLoader
import os

class LaravelBaseGenerator:
    def __init__(self):
        # No need for table_name, class_name, columns, or foreign_keys
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def generate_base_files(self):
        """Generate BaseController and ApiFilter classes."""
        return {
            'ApiFilter.php': self.generate_api_filter(),
            'BaseController.php': self.generate_base_controller(),
        }

    def generate_api_filter(self):
        template = self.env.get_template('/Templates/api_filter_template.php.j2')
        return template.render()

    def generate_base_controller(self):
        template = self.env.get_template('/Templates/base_controller_template.php.j2')
        return template.render()
