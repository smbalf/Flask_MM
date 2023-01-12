"""
The main file called to run medieval merchants
"""
from dotenv import load_dotenv

from root.factory import create_app

if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    app.run()