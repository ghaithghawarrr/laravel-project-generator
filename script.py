import subprocess
import sys
import os
from datetime import datetime  # Import the datetime module

from Generators.Elements.column import Column
from Generators.Elements.foreign_key import ForeignKey

from Generators.controller_generator import ControllerGenerator
from Generators.filter_generator import FilterGenerator
from Generators.migration_generator import MigrationGenerator
from Generators.model_generator import ModelGenerator
from Generators.request_generator import RequestGenerator
from Generators.resource_generator import ResourceGenerator
from Generators.laravel_base_generator import LaravelBaseGenerator

def check_command(command):
    """Check if a command exists in the system PATH."""
    result = subprocess.call(['where', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result == 0

def create_laravel_project(project_name):
    """Create a new Laravel project using Composer."""
    if not check_command('composer'):
        print("Composer is not installed or not found in the system PATH.")
        sys.exit(1)

    try:
        command = ["php", "C:\\composer\\composer.phar", "create-project", "--prefer-dist", "laravel/laravel", project_name]
        print(f"Creating Laravel project '{project_name}'...")
        subprocess.check_call(command)
        print(f"Laravel project '{project_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating Laravel project: {e}")
        sys.exit(1)

def save_file(content, output_dir, file_name):
    """Save a file to the specified directory."""
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Saved: {file_path}")

def save_files(files, project_path, class_name):
    """Save generated files to the appropriate Laravel project directories."""
    directories = {
        "migrations": os.path.join(project_path, 'database', 'migrations'),
        "models": os.path.join(project_path, 'app', 'Models'),
        "filters": os.path.join(project_path, 'app', 'Filters', 'v1'),
        "controllers": os.path.join(project_path, 'app', 'Http', 'Controllers', 'Api', 'V1'),
        "resources": os.path.join(project_path, 'app', 'Http', 'Resources', 'V1'),
        "requests": lambda name: os.path.join(project_path, 'app', 'Http', 'Requests', 'V1', f"{name}Request")
    }
    
    for file_name, content in files.items():
        if "_table" in file_name:
            save_file(content, directories["migrations"], file_name)
        elif class_name + ".php" == file_name:
            save_file(content, directories["models"], file_name)
        elif "Filter" in file_name:
            save_file(content, directories["filters"], file_name)
        elif "Controller" in file_name:
            save_file(content, directories["controllers"], file_name)
        elif "Resource" in file_name or "Collection" in file_name:
            save_file(content, directories["resources"], file_name)
        elif "Request" in file_name:
            save_file(content, directories["requests"](class_name), file_name)

def convert_to_camel_case(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

class LaravelCodeGenerator:
    def __init__(self, table_name, columns, relationships, priority):
        self.table_name = table_name
        self.class_name = convert_to_camel_case(table_name)
        self.columns = columns
        self.foreign_keys = []
        self.relationships = relationships
        self.priority = priority

    def add_foreign_key(self, foreign_key):
        self.foreign_keys.append(foreign_key)

    def generate_all(self):
        generator_classes = {
            "controller": ControllerGenerator(self.class_name),
            "filter": FilterGenerator(self.class_name, self.columns),
            "migration": MigrationGenerator(self.class_name),
            "model": ModelGenerator(self.class_name, self.columns, self.relationships),
            "request": RequestGenerator(self.class_name, self.columns),
            "resource": ResourceGenerator(self.class_name, self.columns, sensitive_fields=['password'], relationships=self.relationships)
        }
        
        for column in self.columns:
            generator_classes["migration"].add_column(column)
        for fk in self.foreign_keys:
            generator_classes["migration"].add_foreign_key(fk)

        return {
            f"{self.class_name}Controller.php": generator_classes["controller"].generate(),
            f"{self.class_name}Filter.php": generator_classes["filter"].generate_filter_class(),
            # Use dynamic date in the migration filename
            f"{get_current_date()}_{self.priority:06d}_create_{self.table_name}_table.php": generator_classes["migration"].generate_migration(),
            f"{self.class_name}.php": generator_classes["model"].generate_model(),
            f"Store{self.class_name}Request.php": generator_classes["request"].generate_store_request(),
            f"BulkStore{self.class_name}Request.php": generator_classes["request"].generate_bulk_store_request(),
            f"Update{self.class_name}Request.php": generator_classes["request"].generate_update_request(),
            f"{self.class_name}Resource.php": generator_classes["resource"].generate_resource(),
            f"{self.class_name}Collection.php": generator_classes["resource"].generate_collection(),
        }

def get_current_date():
    """Get the current date formatted as YYYY_MM_DD."""
    return datetime.now().strftime("%Y_%m_%d")

def main():
    desktop_path = os.path.join(os.path.expanduser("~"), "Lara Projects")
    project_name = os.path.join(desktop_path, "ex-app")
    create_laravel_project(project_name)

    base_generator = LaravelBaseGenerator()
    base_files = base_generator.generate_base_files()
    
    save_file(base_files['BaseController.php'], os.path.join(project_name, 'app', 'Http', 'Controllers'), 'BaseController.php')
    save_file(base_files['ApiFilter.php'], os.path.join(project_name, 'app', 'Filters'), 'ApiFilter.php')

    tables = {
        'users': {
            'priority': 1,
            'columns': [
                Column(name='id', col_type='integer', unique=True, auto_increment=True),
                Column(name='name', col_type='string', size=255, nullable=False),
                Column(name='email', col_type='string', size=255, nullable=False, unique=True),
                Column(name='password', col_type='string', size=255, nullable=False),
                Column(name='created_at', col_type='timestamp', nullable=False),
                Column(name='updated_at', col_type='timestamp', nullable=False),
            ],
            'foreign_keys': [],
            'relationships': [{'method_name': 'posts', 'relationship_type': 'hasMany', 'related_model': 'Post'}]
        },
        'posts': {
            'priority': 2,
            'columns': [
                Column(name='id', col_type='integer', unique=True, auto_increment=True),
                Column(name='user_id', col_type='integer', nullable=False),
                Column(name='title', col_type='string', size=255, nullable=False),
                Column(name='content', col_type='text', nullable=False),
                Column(name='created_at', col_type='timestamp', nullable=False),
                Column(name='updated_at', col_type='timestamp', nullable=False),
            ],
            'foreign_keys': [
                ForeignKey(foreign='user_id', references='id', on='users', on_delete='cascade', on_update='cascade')
            ],
            'relationships': [{'method_name': 'user', 'relationship_type': 'belongsTo', 'related_model': 'User'}]
        }
    }

    for table_name, table_data in tables.items():
        generator = LaravelCodeGenerator(table_name, table_data['columns'], table_data['relationships'], table_data['priority'])
        for fk in table_data['foreign_keys']:
            generator.add_foreign_key(fk)

        files = generator.generate_all()
        save_files(files, project_name, generator.class_name)

if __name__ == "__main__":
    main()
