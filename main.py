import subprocess



def install_package(package_name):

    try:

        # Tries to use pip3 first, falls back to pip if pip3 is not available

        pip_command = "pip3" if subprocess.call(["which", "pip3"]) == 0 else "pip"

        subprocess.check_call([pip_command, "install", package_name])

        print(f"[Package Chaos]: {package_name} installed successfully!")

    except subprocess.CalledProcessError:

        print(f"[Package Chaos]: Failed to install {package_name}!")



def main():

    required_packages = ["requests", "dnspython"]

    for package in required_packages:

        install_package(package)

    # Your existing code goes here



if __name__ == "__main__":

    main()

