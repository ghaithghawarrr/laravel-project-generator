from jinja2 import Environment, FileSystemLoader
import os
from .Elements.column import Column

class RequestGenerator:
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns
        self.class_name = table_name.capitalize()
        self.env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

    def generate_store_request(self):
        rules = self._generate_rules(self.columns)
        template = self.env.get_template('/Templates/store_request_template.php.j2')

        return template.render(
            class_name=self.class_name,
            rules=rules
        )

    def generate_bulk_store_request(self):
        rules = self._generate_rules(self.columns, bulk=True)
        template = self.env.get_template('/Templates/bulk_store_request_template.php.j2')

        return template.render(
            class_name=self.class_name,
            rules=rules
        )

    def generate_update_request(self):
        rules_put = self._generate_rules(self.columns)
        rules_patch = self._generate_rules(self.columns, sometimes=True)
        template = self.env.get_template('/Templates/update_request_template.php.j2')

        return template.render(
            class_name=self.class_name,
            rules_put=rules_put,
            rules_patch=rules_patch
        )

    def _generate_rules(self, columns, bulk=False, sometimes=False):
        rules = ""
        prefix = "*." if bulk else ""
        conditional = "'sometimes', " if sometimes else ""

        for column in columns:
            rule = f"'{prefix}{column.name}' => [{conditional}'{self._get_rule_type(column)}', "

            if column.col_type == 'string' and column.size:
                rule += f"'max:{column.size}', "
            elif column.col_type in ['integer', 'decimal']:
                rule += "'min:0', "

            if column.name.endswith('_id'):
                rule += f"'exists:{column.name[:-3]},{column.name[-2:]}'"
            elif column.col_type == 'boolean':
                rule += "'boolean'"
            else:
                rule += f"'{column.col_type}'"

            if column.nullable:
                rule = rule.replace("'required'", "'nullable'")

            rule = rule.rstrip(", ") + "],\n"
            rules += f"            {rule}"

        return rules.rstrip(",\n")

    def _get_rule_type(self, column):
        if column.col_type in ['string', 'text']:
            return 'required' if not column.nullable else 'nullable'
        if column.col_type == 'integer':
            return 'integer'
        if column.col_type == 'decimal':
            return 'numeric'
        if column.col_type == 'boolean':
            return 'boolean'
        return 'required'
