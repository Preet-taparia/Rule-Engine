# Rule Engine

Creating a virtual environment in Python is straightforward. Here’s a step-by-step guide:

### Using `venv` (Python 3.3 and above)

1. **Open a Terminal or Command Prompt**:
   - On Windows, you can use Command Prompt or PowerShell.
   - On macOS or Linux, use the Terminal.

2. **Navigate to Your Project Directory**:
   Use the `cd` command to change to your project directory. For example:
   ```bash
   cd path/to/your/project
   ```

3. **Create the Virtual Environment**:
   Run the following command to create a virtual environment named `venv` (you can name it anything):
   ```bash
   python -m venv venv
   ```
   This will create a folder named `v     env` in your project directory containing the virtual environment.

4. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   After activation, you should see the environment name (e.g., `(venv)`) in your command prompt, indicating that the virtual environment is active.

5. **Install Packages**:
   Now that the virtual environment is activated, you can install packages using `pip`. For example:
   ```bash
   pip install requests
   ```

6. **Deactivate the Virtual Environment**:
   When you’re done working, you can deactivate the virtual environment by simply running:
   ```bash
   deactivate
   ```

### Notes:
- Always activate your virtual environment before working on your project to ensure that you’re using the correct package versions.
- You can create a `requirements.txt` file to keep track of your dependencies. Run the following command to generate it:
  ```bash
  pip freeze > requirements.txt
  ```
- Later, you can install all dependencies from `requirements.txt` with:
  ```bash
  pip install -r requirements.txt
  ```

Let me know if you need further help!