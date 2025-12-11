import os
from pathlib import Path

def get_airflow_env():
    """
    Sets up the environment variables for running Airflow.
    Returns a tuple of (environment dict, airflow_home path).
    """
    # Get the project root directory (assuming this script is in scripts/)
    project_root = Path(__file__).resolve().parent.parent
    airflow_home = project_root / "airflow"
    
    env = os.environ.copy()
    env["AIRFLOW_HOME"] = str(airflow_home)
    
    # Add project root to PYTHONPATH so DAGs can import local modules
    python_path = env.get("PYTHONPATH", "")
    # Prepend project root to PYTHONPATH
    env["PYTHONPATH"] = f"{project_root}:{python_path}" if python_path else str(project_root)
    
    return env, airflow_home
