import subprocess


def install_package(package_name):
    subprocess.check_call(["pip", "install", package_name])


package_list = ["fastapi", "uvicorn", "hashlib", "starlette", "abc", "sqlalchemy"]

for package in package_list:
    try:
        install_package(package)
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")
