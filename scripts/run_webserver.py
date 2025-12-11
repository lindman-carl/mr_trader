#!/usr/bin/env python3
import subprocess
import sys
import argparse
try:
    from .common import get_airflow_env
except ImportError:
    from common import get_airflow_env

def main():
    parser = argparse.ArgumentParser(description="Run Airflow Webserver")
    parser.add_argument("-p", "--port", type=int, default=9090, help="Port to run the webserver on")
    args = parser.parse_args()

    env, airflow_home = get_airflow_env()
    print(f"Starting Airflow Webserver on port {args.port} with AIRFLOW_HOME={airflow_home}")
    
    try:
        subprocess.run(["airflow", "webserver", "--port", str(args.port)], env=env, check=True)
        
    except KeyboardInterrupt:
        print("\nStopping Airflow Webserver...")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running Airflow Webserver: {e}")
        sys.exit(1)
        
    except FileNotFoundError:
        print("Error: 'airflow' command not found. Make sure it is installed in your environment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
