class DataType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class BigInt(DataType):
    def __init__(self):
        super().__init__("bigint", "A large integer value")


class Binary(DataType):
    def __init__(self):
        super().__init__("binary", "A binary string")


class Blob(DataType):
    def __init__(self):
        super().__init__("blob", "Binary Large Object")


class Boolean(DataType):
    def __init__(self):
        super().__init__("boolean", "A boolean value (true/false)")


class Char(DataType):
    def __init__(self):
        super().__init__("char", "A fixed-length string")


class Date(DataType):
    def __init__(self):
        super().__init__("date", "A date value (YYYY-MM-DD)")


class DateTime(DataType):
    def __init__(self):
        super().__init__("datetime", "A date and time value (YYYY-MM-DD HH:MM:SS)")


class Decimal(DataType):
    def __init__(self):
        super().__init__("decimal", "A decimal number")


class Double(DataType):
    def __init__(self):
        super().__init__("double", "A double-precision floating point number")


class Enum(DataType):
    def __init__(self):
        super().__init__("enum", "An enumerated type (set of predefined values)")


class Float(DataType):
    def __init__(self):
        super().__init__("float", "A single-precision floating point number")


class Int(DataType):
    def __init__(self):
        super().__init__("int", "An integer value")


class Json(DataType):
    def __init__(self):
        super().__init__("json", "A JSON-formatted value")


class LongText(DataType):
    def __init__(self):
        super().__init__("longtext", "A long text field")


class MediumText(DataType):
    def __init__(self):
        super().__init__("mediumtext", "A medium text field")


class Set(DataType):
    def __init__(self):
        super().__init__("set", "A set of predefined values")


class SmallInt(DataType):
    def __init__(self):
        super().__init__("smallint", "A small integer value")


class Text(DataType):
    def __init__(self):
        super().__init__("text", "A text field")


class Time(DataType):
    def __init__(self):
        super().__init__("time", "A time value (HH:MM:SS)")


class Timestamp(DataType):
    def __init__(self):
        super().__init__("timestamp", "A timestamp value (YYYY-MM-DD HH:MM:SS)")


class TinyInt(DataType):
    def __init__(self):
        super().__init__("tinyint", "A tiny integer value")


class UnsignedBigInteger(DataType):
    def __init__(self):
        super().__init__("unsignedBigInteger", "An unsigned large integer value")


class UnsignedInteger(DataType):
    def __init__(self):
        super().__init__("unsignedInteger", "An unsigned integer value")


class Varchar(DataType):
    def __init__(self):
        super().__init__("varchar", "A variable-length string")


class Year(DataType):
    def __init__(self):
        super().__init__("year", "A year value (YYYY)")


class Geometry(DataType):
    def __init__(self):
        super().__init__("geometry", "A geometry data type (e.g., point, line, polygon)")


class UUID(DataType):
    def __init__(self):
        super().__init__("uuid", "A universally unique identifier (UUID)")


class Bit(DataType):
    def __init__(self):
        super().__init__("bit", "A bit field (used for storing bits)")


# Utility function to get all data types
def get_all_data_types():
    return [
        BigInt(), Binary(), Blob(), Boolean(), Char(), Date(), DateTime(),
        Decimal(), Double(), Enum(), Float(), Int(), Json(), LongText(),
        MediumText(), Set(), SmallInt(), Text(), Time(), Timestamp(),
        TinyInt(), UnsignedBigInteger(), UnsignedInteger(), Varchar(),
        Year(), Geometry(), UUID(), Bit()
    ]


# Column class updated to use DataType classes
class Column:
    def __init__(self, name, col_type, size=None, nullable=False, default=None, virtual_as=None):
        self.name = name
        self.col_type = col_type
        self.size = size
        self.nullable = nullable
        self.default = default
        self.virtual_as = virtual_as
        self._validate_type()
    
    def _validate_type(self):
        valid_types = {dtype.name for dtype in get_all_data_types()}
        if self.col_type not in valid_types:
            raise ValueError(f"Invalid column type: {self.col_type}. Must be one of {', '.join(valid_types)}.")
    
    def generate_definition(self):
        definition = f"$table->{self.col_type}('{self.name}'"
        if self.size:
            definition += f", {self.size}"
        definition += ")"
        if self.nullable:
            definition += "->nullable()"
        if self.default is not None:
            if isinstance(self.default, str):
                definition += f"->default('{self.default}')"
            else:
                definition += f"->default({self.default})"
        if self.virtual_as:
            definition += f"->virtualAs('{self.virtual_as}')"
        return definition + ";"
    
    
    
    
    

mysql_data_types_extended = [
    {"type": "bigint", "description": "A large integer value"},
    {"type": "binary", "description": "A binary string"},
    {"type": "blob", "description": "Binary Large Object"},
    {"type": "boolean", "description": "A boolean value (true/false)"},
    {"type": "char", "description": "A fixed-length string"},
    {"type": "date", "description": "A date value (YYYY-MM-DD)"},
    {"type": "datetime", "description": "A date and time value (YYYY-MM-DD HH:MM:SS)"},
    {"type": "decimal", "description": "A decimal number"},
    {"type": "double", "description": "A double-precision floating point number"},
    {"type": "enum", "description": "An enumerated type (set of predefined values)"},
    {"type": "float", "description": "A single-precision floating point number"},
    {"type": "int", "description": "An integer value"},
    {"type": "integer", "description": "An integer value (same as 'int')"},
    {"type": "json", "description": "A JSON-formatted value"},
    {"type": "longtext", "description": "A long text field"},
    {"type": "mediumtext", "description": "A medium text field"},
    {"type": "set", "description": "A set of predefined values"},
    {"type": "smallint", "description": "A small integer value"},
    {"type": "text", "description": "A text field"},
    {"type": "time", "description": "A time value (HH:MM:SS)"},
    {"type": "timestamp", "description": "A timestamp value (YYYY-MM-DD HH:MM:SS)"},
    {"type": "tinyint", "description": "A tiny integer value"},
    {"type": "unsignedBigInteger", "description": "An unsigned large integer value"},
    {"type": "unsignedInteger", "description": "An unsigned integer value"},
    {"type": "varchar", "description": "A variable-length string"},
    {"type": "year", "description": "A year value (YYYY)"},
    {"type": "geometry", "description": "A geometry data type (e.g., point, line, polygon)"},
    {"type": "point", "description": "A point in 2D space"},
    {"type": "linestring", "description": "A line string in 2D space"},
    {"type": "polygon", "description": "A polygon in 2D space"},
    {"type": "multipoint", "description": "A collection of points"},
    {"type": "multilinestring", "description": "A collection of line strings"},
    {"type": "multipolygon", "description": "A collection of polygons"},
    {"type": "geometrycollection", "description": "A collection of geometries"},
    {"type": "uuid", "description": "A universally unique identifier (UUID)"},
    {"type": "bit", "description": "A bit field (used for storing bits)"}
]