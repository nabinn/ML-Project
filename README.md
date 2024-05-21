## Steps to run the Chatbot Application

## Step 1. Create a new python virtual enviornment

Follow these instructions to create a virtual environment for a specified version of Python:

### Prerequisites

- Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Verify that `pip` is installed by running `pip --version` in your terminal or command prompt.

### Step 1.1: Install `virtualenv`

If not already installed, you need to install `virtualenv` using pip:

```bash
pip install virtualenv
```

### Step 1.2: Create the Virtual Environment

Create a virtual environment specifying the path to the Python interpreter for the version you wish to use. Replace `path/to/python` with the actual path and `myenv` with your desired environment name:

```bash
virtualenv -p /path/to/python myenv
```

- **Example for Windows**: If Python 3.8 is installed at `C:\Python38\python.exe`:

  ```bash
  virtualenv -p C:\Python38\python.exe myenv
  ```

- **Example for macOS/Linux**: If Python 3.8 is installed and the executable is named `python3.8`:

  ```bash
  virtualenv -p python3.8 myenv
  ```

### Step 1.3: Activate the Virtual Environment

Activate the newly created virtual environment:

- **On Windows**:

  ```bash
  myenv\Scripts\activate
  ```

- **On macOS/Linux**:

  ```bash
  source myenv/bin/activate
  ```

### Step 1.4: Verify Python Version

Check the Python version to ensure the correct version is activated:

```bash
python --version
```

### Step 1.5: Deactivate the Environment

To stop using the virtual environment and revert to the default Python settings:

```bash
deactivate
```

This completes the setup of a Python virtual environment with your specified version.


## Step 2: Install necessary packages
Activate the virtual environment and install packages using this command.
``` pip install -r requirements.txt ```

## Step 3: Run the Streamlit application
Run  the application with the following command -
``` cd chatbot && streamlit run app.py```

---
Notes:
- It downloads the Hugging face models and caches inside the `models` folders when you run the application for the first time. So, the first run will be slower. In subsequent runs, it will simply load the downloaded models stored locally.

- If it shows errors related to hugging face transformers libarary, a latest version can be installed directly using the following.
```pip install git+https://github.com/huggingface/transformers```
