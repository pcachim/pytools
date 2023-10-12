#!/bin/zsh

# Check if a directory name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

# Get the directory name from the first argument
dir_name=$1

# Check if the directory already exists
if [ -d "$dir_name" ]; then
    echo "Directory '$dir_name' already exists. Please choose a different name."
    exit 1
fi

# Create the directory
mkdir "$dir_name"

# Change to the new directory
cd "$dir_name"

# Create a Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

pip install --upgrade pip
pip install pip-tools


# Create a requirements.txt file
echo > requirements.txt
echo "pandas" >> requirements.in
#echo "scipy" >> requirements.in
#echo "geopandas" >> requirements.in
#echo "matplotlib" >> requirements.in
#echo "folium" >> requirements.in
#echo "seaborn" >> requirements.in
#echo "scikit-learn" >> requirements.in

pip-compile requirements.in
pip-sync requirements.txt


# Create a requirements-dev.txt file
echo > requirements-dev.in
echo "streamlit" >> requirements-dev.in
echo "streamlit-folium" >> requirements-dev.in
echo "streamlit-extras" >> requirements-dev.in
echo "watchdog" >> requirements-dev.in
#echo "jupyterlab" >> requirements.in
#echo "pytest" >> requirements-dev.txt

pip-compile requirements-dev.in
pip-sync requirements-dev.txt


# Create a .gitignore file
echo > .gitignore
echo ".venv" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.py[cod]" >> .gitignore

# Initialize a git repository
git init
git add .
git commit -m "Initial commit"

# Provide instructions to the user
echo "Created directory: $dir_name"
echo "Python virtual environment (venv) is set up in '$dir_name/.venv'"
echo "To activate the venv, use 'source $dir_name/.venv/bin/activate'"
echo "To deactivate the venv, simply run 'deactivate'"