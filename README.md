```markdown
# Tech Gear Inventory Module
```

## Overview

The Tech Gear Inventory module provides functionality to import product data from an Excel file into Odoo. This module supports the following features:

- Parsing an Excel file containing product data (Product Name, Category, Price, Quantity).
- Updating the Odoo database with the parsed product data.
- Creating or updating products.
- Creating or updating product categories.
- Managing stock quantities for the imported products.

## Installation

### Prerequisites

Ensure that you have the following installed:

- Odoo 17.0 or later
- Python dependencies:
  - `xlrd` for reading Excel files

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/JetonStojku/odoo_project.git
   ```

2. **Place the Module**

   Place the `tech_gear_inventory` folder in your Odoo `addons` directory.
   Include `/path/to/your/addons/odoo_project/` in the `addons_path` configuration in `odoo.conf`.

3. **Update Module List**

   Start your Odoo server and update the module list:

   ```sh
   ./odoo-bin -c /path/to/your/odoo.conf -u all
   ```

4. **Install the Module**

   Go to the Apps menu in Odoo, search for `Tech Gear Inventory`, and install the module.

## Usage

1. **Upload Excel File**

   Go to the `Inventory -> Products -> Import Wizard` menu and select the option to import products.

2. **Select Excel File**

   Choose the Excel file that contains your product data. The Excel file must have the following columns in this exact order:
   - `Product Name`
   - `Category`
   - `Price`
   - `Quantity`

3. **Import Products**

   Click on the `Import Products` button to start the import process. The module will parse the Excel file, create or update the products and categories, and set the stock quantities accordingly.

## Functional Requirements

### Excel File Parsing

Ensure that the module correctly parses an Excel file and updates the database accordingly. The Excel file must have the following columns:

- `Product Name`
- `Category`
- `Price`
- `Quantity`

### Error Handling

The module will raise an error if:

- The file is not uploaded.
- The required headers are missing or not in the correct order.

### Example

An example Excel file might look like this:

| Product Name | Category | Price | Quantity |
|--------------|----------|-------|----------|
| Product A    | Category1| 10.0  | 100      |
| Product B    | Category2| 20.0  | 200      |

## Testing

To run the tests for this module, follow these steps:

1. **Configure Testing in VSCode**

   Ensure you have the following launch configuration in your `.vscode/launch.json`:

   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Odoo: Test tech_gear_inventory",
         "type": "python",
         "request": "launch",
         "program": "${workspaceFolder}/odoo-bin",
         "args": [
           "-c", "${workspaceFolder}/odoo.conf",
           "-d", "your_database_name",
           "--log-level=debug",
           "--test-enable",
           "--stop-after-init",
           "-i", "tech_gear_inventory"
         ],
         "pythonPath": "path\\to\\your\\interpreter\\python.exe",
         "console": "integratedTerminal",
         "env": {
           "ODOO_RC": "${workspaceFolder}/odoo.conf"
         }
       }
     ]
   }
   ```

2. **Run the Tests**

   Open the Command Palette in VSCode (Ctrl+Shift+P or F1) and select `Debug: Start Debugging` or press F5. Choose the configuration `Odoo: Test tech_gear_inventory`.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
