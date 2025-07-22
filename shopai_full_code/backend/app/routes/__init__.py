from importlib import import_module
from pathlib import Path

def register_routes(app):
    routes_path = Path(__file__).parent
    for file in routes_path.glob("*.py"):
        if file.name.startswith("_"):
            continue
        module = import_module(f"app.routes.{file.stem}")
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)
