# foreign_key.py
class ForeignKey:
    def __init__(self, foreign, references, on, on_delete='cascade', on_update='cascade'):
        self.foreign = foreign
        self.references = references
        self.on = on
        self.on_delete = on_delete
        self.on_update = on_update

    def get_definition(self):
        return f"$table->foreign('{self.foreign}')->references('{self.references}')->on('{self.on}')->onDelete('{self.on_delete}')->onUpdate('{self.on_update}');"
