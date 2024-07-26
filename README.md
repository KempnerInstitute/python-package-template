# Python Packaging User Guide and Template

This is a guide to packaging and distributing Python code. [PYPA (Python Packaging Authority)](https://www.pypa.io/en/latest/) is a working group that maintains a core set of software projects used in Python packaging. The PYPA publishes the [Python Packaging User Guide](https://packaging.python.org/en/latest/), which is the official guide to packaging Python code. 


## Starting a new project

The following are the basic steps to start a new Python project:

1. Create the project directory structure

  - Set up your project directory following the [flat structure](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) convention. 


    ```bash
    my_package/
    ├── my_package/
    │   ├── __init__.py
    │   └── module.py
    ├── tests/
    |   ├── __init__.py
    │   └── test_module.py
    ├── LICENSE
    ├── README.md
    └── pyproject.toml
    ```
2. Intialize a Git repository

    ```bash
    cd my_package
    git init
    ```
3. Create `pyproject.toml` file

  - Define the metadata for your project in the pyproject.toml file. The file contains three sections: `build-system`, `project`, and `tool`. The `build-system` section specifies the build backend and the required build dependencies.The `project` section specifies the project metadata. The `tool` section specifies the build tool to use. The first two sections are required, and the last section is optional. 

  - The following file shows an example of a `pyproject.toml` file: 

    ```toml
    [build-system]
    requires = ["setuptools", "wheel"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "my_package"
    version = "0.1.0"
    description = "A sample Python package"
    authors = [
    { name = "Your Name", email = "your.email@example.com" }
    ]
    license = { file = "LICENSE" }
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ]
    dependencies = []

    ```

  - Note that you can also use `setup.py` file to define the metadata for your project. However, the `pyproject.toml` file is the recommended way to define the metadata for your project. In case of adding C extensions, you can use `setup.py` file.

4. Add License file

  - Add a license file to your project. The license file should contain the license text. You can use the [MIT License](https://opensource.org/licenses/MIT) as a template for your license file.
  - Visit [Choose a License](https://choosealicense.com/) to select an appropriate license for your project.

5. Add README file

- Add a README file to your project. The README file should contain the project description, installation instructions, usage instructions, and other relevant information about the project. 

6. Add `__init__.py` file

- Add an `__init__.py` file to the package directory. Please see the folder structure at step 1. The `__init__.py` file can be empty or contain initialization code for the package.

7. Add a module file

- Add a module file to the package directory. The module file contains the code for your package. You can add multiple module files to the package directory.

8. Add a test file

- Add a test file to the tests directory. The test file contains the test code for your package. There are two types of tests: unit tests and integration tests. You can use the `unittest` module or the `pytest` library to write tests for your package.
- It is a good practice to write tests while developing your package. Writing tests helps you to ensure that your package works as expected and to catch bugs early in the  process.

9. Add a `.gitignore` file

- Add a `.gitignore` file to your project. The `.gitignore` file specifies the files and directories that should be ignored by Git. 

10. Install your package in editable mode

- Install your package in editable mode using the following command:

  ```bash
  pip install -e .
  ```

Please see the [Python Packaging Template](python_packaging_template) for a template that you can use to start a new Python project. 

## Converting an existing project to a package

1. Organize the Directory Structure

  - Ensure your current project follows the standard flat directory structure as shown above.
  - Make sure that all files are saved and pushed to the repository, if applicable.

2. Add pyproject.toml

  - Create and configure the pyproject.toml file with appropriate metadata.

3. Add License and Readme Files

  - Ensure your project includes a LICENSE file and a README.md file.

4. Move Source Code into Package Directory

  - Refactor your code into the my_package directory to align with best practices.

5. Write or Update Tests

  - Create or update test scripts in the tests directory.

6. Install and Test Your Package

  - Install your package locally and run tests to verify everything works correctly.

7. Version Control

  - Initialize or update your Git repository with the refactored project structure.