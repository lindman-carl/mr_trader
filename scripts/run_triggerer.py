#!/home/gmk/dev/mr_trader/.venv/bin/python
import subprocess
import sys
try:
    from .common import get_airflow_env
except ImportError:
    from common import get_airflow_env

def main():
    env, airflow_home = get_airflow_env()
    print(f"Starting Airflow Triggerer with AIRFLOW_HOME={airflow_home}")
    
    try:
        subprocess.run(["airflow", "triggerer"], env=env, check=True)
        
    except KeyboardInterrupt:
        print("\nStopping Airflow Triggerer...")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running Airflow Triggerer: {e}")
        sys.exit(1)
        
    except FileNotFoundError:
        print("Error: 'airflow' command not found. Make sure it is installed in your environment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
