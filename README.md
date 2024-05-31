## Steps to run the Chatbot Application

## Step 1. Create a new virtual enviornment and install necessary packages

Follow these instructions to create a virtual environment for a specified version of Python:

### Prerequisites

- Make sure [Python](https://www.python.org/downloads/) and [Anaconda](https://www.anaconda.com/) are installed on your machine. Follow the install instructions if the are not installed.
- You can use following commands to check if they are installed.
    - ```python --version```
    - ```conda --version```


### Step 1.1: Create new virtual environment using Anaconda

The following command shows how to create new virtual environment with Python 3.8 in Anaconda. The name of the environment is `myenv`. This step needs to be done **only once** at the beginning.

```bash
conda create -n myenv python=3.8
```

### Step 1.2: Activate the Virtual Environment and install necessary packages
Once the virtual environment is created you can activate it and install necessary packages. 
This step also needs to be done **only once** at the beginning. 
Go to the root directory of the project (where you can see `requirements.txt` file) and run the following command.
```bash
source activate myenv && pip install -r requirements.txt
```

## Step 2: Run the Streamlit application
To run the application you need to navigate to the root directory of the project. Once you are there you need to activate the virtual ennvironment and run the streamlit command. Here is the command to do so -
``` bash
source activate myenv && \
cd chatbot && streamlit run app.py
```

    Note: You need to do this every time to run the application. Step 1 can be skipped once the virtual environment is created and necessary packages are installed. 

---
Notes:
- It downloads the Hugging face models and caches inside the `models` folders when you run the application for the first time. So, the first run will be slower. In subsequent runs, it will simply load the downloaded models stored locally.

- If it shows errors related to hugging face transformers libarary, a latest version can be installed directly using the following.
```pip install git+https://github.com/huggingface/transformers```
