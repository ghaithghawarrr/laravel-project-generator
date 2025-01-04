# Laravel Project Generator 🚀

A powerful and flexible code generator for Laravel projects that helps you quickly scaffold common components with best practices built-in.

## Features ✨

- 🔥 **CRUD Operations** - Generates complete CRUD operations with validation
- 📦 **Bulk Operations Support** - Built-in support for bulk create and delete operations
- 🛡️ **Advanced Filtering** - Sophisticated query filtering with security measures
- 🗑️ **Soft Deletes** - Optional soft delete support for models
- ⏰ **Timestamp Handling** - Configurable timestamp formats and handling
- ✅ **Input Validation** - Comprehensive request validation with custom messages
- 🔒 **Security** - SQL injection prevention and input sanitization
- 📝 **API Versioning** - Built-in support for API versioning
- 💾 **Database Transactions** - Automatic transaction handling for bulk operations

## Installation 🔧

1. Clone the repository:
```bash
git clone https://github.com/yourusername/laravel-project-generator.git
```

2. Navigate to the project directory:
```bash
cd laravel-project-generator
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage 📚

### Basic Usage

```bash
python script.py generate:crud YourModelName
```

### Available Commands

1. Generate CRUD:
```bash
python script.py generate:crud ModelName
```

2. Generate Model:
```bash
python script.py generate:model ModelName
```

3. Generate Controller:
```bash
python script.py generate:controller ModelName
```

4. Generate Filter:
```bash
python script.py generate:filter ModelName
```

### Configuration Options

You can customize the generation process by providing additional options:

- `--with-soft-deletes` - Add soft delete support
- `--api-version=v2` - Specify API version
- `--timestamps=false` - Disable timestamps
- `--bulk-operations` - Add bulk operation support

Example:
```bash
python script.py generate:crud User --with-soft-deletes --api-version=v2 --bulk-operations
```

## Generated Components 🏗️

### 1. Model
- Configurable timestamps
- Soft delete support
- Fillable/Guarded attributes
- Relationship definitions
- Date formatting options

### 2. Controller
- Standard CRUD operations
- Bulk create/delete operations
- Transaction handling
- Resource responses
- Error handling

### 3. Requests
- Input validation
- Custom error messages
- Data transformation
- Bulk operation validation

### 4. Filters
- Query parameter filtering
- Operator mapping
- SQL injection prevention
- Error handling
- Custom column mapping

## Best Practices 👌

The generator follows Laravel best practices including:

- PSR-4 autoloading standards
- SOLID principles
- RESTful API conventions
- Proper error handling
- Database transaction management
- Input validation and sanitization
- API versioning
- Resource transformation

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬

If you have any questions or need help, please:
1. Check the documentation
2. Open an issue
3. Contact the maintainers

## Acknowledgments 🙏

- Laravel community for inspiration and best practices
- Contributors who helped improve the project
- Everyone who has submitted issues and helped make this project better

---

Made with ❤️ by [Your Name]
