# Home Dashboard Project

## Python notes
- Indent all files with 4 spaces - Python is particular about this
- Use the virtual environment in the venv folder

### Installing Python Dependencies
- Create a virtual environment in the project directory: `$python3 -m venv venv`
- Activate the virtual environment:
    - On Mac/Linux `$ source venv/bin/activate`
- Install with `(venv) $ pip install -r requirements.txt`
- If you install a new package, create a new requirements file with `(venv) $ pip freeze > requirements.txt`

## Project Structure
- A backend web application in api/
- A frontend web application in ui/
- Maybe a generator in generator/
