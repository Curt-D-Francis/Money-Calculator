import subprocess
import sys
import os

def install_requirements():
    print("Installing required packages...")
    try:
        # Upgrade pip first
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        
        # Install requirements
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        
        print("\nInstallation successful! You can now run the program using 'python main.py'")
        
        # Ask if user wants to run the program now
        run_now = input("\nWould you like to run the program now? (y/n): ")
        if run_now.lower() == 'y':
            subprocess.call([sys.executable, 'main.py'])
            
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    install_requirements()