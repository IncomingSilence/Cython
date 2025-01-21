import subprocess
import time
import os

def run_script(script_path):
    start_time = time.time()
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    execution_time = time.time() - start_time
    return result.stdout, result.stderr, execution_time

if __name__ == "__main__":
    # Define the paths to the scripts
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cython_script_path = os.path.join(base_dir, "run_cython.py")
    python_script_path = os.path.join(base_dir, "Python_Fraktal.py")
    fraktal_image_path = os.path.join(base_dir, "fraktal.png")  # Pfad zum Fraktalbild

    #print(f"Python script path: {python_script_path}")
    #print(f"Cython script path: {cython_script_path}")

# Run the Cython script
    cython_output, cython_error, cython_time = run_script(cython_script_path)
    if cython_error:
        print(f"Error running Cython script:\n{cython_error}")
    else:
        #print(cython_output)
        #print(f"Cython execution time: {cython_time:.2f} seconds")
        pass

    # Run the Python script
    python_output, python_error, python_time = run_script(python_script_path)
    if python_error:
        print(f"Error running Python script:\n{python_error}")
    else:
        #print(python_output)
        #print(f"Python execution time: {python_time:.2f} seconds")
        pass

    # Compare execution times
    if not python_error and not cython_error:
        print()
        print(f"\033[94mPython execution time: {python_time:.2f} seconds\033[0m")  # Blue text
        print(f"\033[94mCython execution time: {cython_time:.2f} seconds\033[0m")  # Blue text
        print()
        print(f"\033[92mCython is {python_time / cython_time:.2f} times faster than Python\033[0m")  # Green text

    # Open the Fraktal image
    if os.path.exists(fraktal_image_path):
        if os.name == 'posix':  # Linux or macOS
            subprocess.run(['xdg-open', fraktal_image_path])
        elif os.name == 'nt':  # Windows
            subprocess.run(['mspaint', fraktal_image_path])
    else:
        print(f"Fraktal image not found at {fraktal_image_path}")