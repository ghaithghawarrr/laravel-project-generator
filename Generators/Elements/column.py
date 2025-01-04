# column.py
class Column:
    def __init__(self, name, col_type, **options):
        self.name = name
        self.col_type = col_type
        self.options = options

        # Initialize attributes based on options
        self.size = options.get('size', None)
        self.unique = options.get('unique', False)
        self.nullable = options.get('nullable', False)  # Add this line
        self.default = options.get('default', None)

    def get_definition(self):
        definition = f"$table->{self.col_type}('{self.name}'"
        
        if self.size is not None:
            definition += f", {self.size}"
        
        if self.nullable:
            definition += ")->nullable()"
        else:
            definition += ")"
        
        if self.unique:
            definition += "->unique()"

        if self.default is not None:
            definition += f"->default('{self.default}')"

        return definition + ";"
