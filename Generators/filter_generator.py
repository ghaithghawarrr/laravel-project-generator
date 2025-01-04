from jinja2 import Environment, FileSystemLoader
import os
from .Elements.column import Column

class FilterGenerator:
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns
        self.class_name = table_name.capitalize()
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def generate_filter_class(self):
        safe_parms = self._generate_safe_parms(self.columns)
        column_map = self._generate_column_map(self.columns)
        operator_map = self._generate_operator_map()

        template = self.env.get_template('/Templates/filter_template.php.j2')

        return template.render(
            class_name=self.class_name,
            safe_parms=safe_parms,
            column_map=column_map,
            operator_map=operator_map
        )

    def _generate_safe_parms(self, columns):
        safe_parms = ""
        common_operators = ['eq', 'ne']
        numeric_operators = common_operators + ['lt', 'gt', 'lte', 'gte']
        string_operators = common_operators + ['like']

        for column in columns:
            operators = numeric_operators if column.col_type in ['integer', 'decimal'] else string_operators
            operators_str = "', '".join(operators)
            safe_parms += f"        '{column.name}' => ['{operators_str}'],\n"

        return safe_parms.rstrip(",\n")

    def _generate_column_map(self, columns):
        column_map = ""
        for column in columns:
            camel_case_name = ''.join([word.capitalize() for word in column.name.split('_')])
            camel_case_name = camel_case_name[0].lower() + camel_case_name[1:]
            if column.name != camel_case_name:
                column_map += f"        '{camel_case_name}' => '{column.name}',\n"

        return column_map.rstrip(",\n")

    def _generate_operator_map(self):
        operator_map = {
            'eq': '=',
            'lt': '<',
            'gt': '>',
            'lte': '<=',
            'gte': '>=',
            'like': 'LIKE',
            'ne': '<>',  # Not equal
        }
        operator_map_str = ""
        for key, value in operator_map.items():
            operator_map_str += f"        '{key}' => '{value}',\n"
        return operator_map_str.rstrip(",\n")
