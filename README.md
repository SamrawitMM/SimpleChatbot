# Project Setup Instructions

## Clone the Repository

To clone the repository from the `task3-integration` branch, use the following command:

```sh
git clone --branch task3-integration --single-branch https://github.com/OmdenaAI/IREX-Colombia-DR.git
```

Navigate to the root directory

```sh
cd IREX-Colombia-DR
```

Create and Activate a Virtual Environemtn

1. Install virtualenv (if it's not already installed):

```sh
pip install virtualenv
```

2. Create a virtual environment:
```sh
virtualenv venv
```


Alternatively, you can create a virtual environment using:

```sh
python -m venv venv
```

Activate the virtual environment based on your operating system:

On Windows

```sh
venv\Scripts\activate
```

On macOS or Linux:

```sh
source venv/bin/activate
```


Run the Project

```sh
docker-compose up --build
```

Working on your own branch

Crate and swith to a new branch to avoid conflicts

```sh
git checkout -b yourname_branch
```