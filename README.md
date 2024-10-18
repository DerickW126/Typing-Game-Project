# Typing Speed Test Game

A Python-based Typing Speed Test application that pulls random sentences from the New York Times using their **Top Stories API**. This app measures your typing speed, accuracy, and words per minute (WPM) in a fun and interactive way. The project also demonstrates **good practices** by securing API keys and using dependency management with `requirements.txt`.

## **Demo**

![Demo Gif](Demo%20Gif.gif)

---

## **Features**

- **Interactive Typing Test:** Measure your WPM and typing accuracy in real-time.
- **Dynamic Content:** Sentences are fetched from the New York Times Top Stories API.
- **Responsive UI:** Smooth input handling and user feedback.
- **Reset Functionality:** Start a new session with one click after completing a test.
- **Secure API Key Management:** Uses environment variables to protect sensitive data.

---

## **Prerequisites**

Make sure you have the following installed:

- **Python 3.x**
- **Pygame** library
- **Requests** library
- **python-dotenv** library

---

## **Project Setup**

### **1. Clone the Repository via SSH**

Ensure that you have set up an SSH key. If you haven’t done this already, follow the [SSH Key Setup Instructions](#ssh-key-setup).

Clone the repository using SSH:

```bash
git clone git@github.com:<your-username>/typing-speed-test.git
cd typing-speed-test
```

### **2. Set Up Your API Key**

1. **Create a `.env` file** in the project root directory:
```bash
NYT_API_KEY=your_nyt_api_key_here
```
2. **Get your API key** from the [NYT Developer Portal](https://developer.nytimes.com/).

3. **Ensure the `.env` file is ignored by Git** to keep it secure. If you don't have a `.gitignore` file yet, create one and add the following line:
```bash
.env
```

4. **Load the API key in your code** using `python-dotenv`. Make sure to install the library:
```bash
pip install python-dotenv
```
### **5. Update your Python code to read the API key from the environment:
```bash
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the NYT API key from the environment
API_KEY = os.getenv('NYT_API_KEY')

if not API_KEY:
    raise ValueError("NYT_API_KEY is not set. Please add it to your .env file.")
```

### **3. Install Dependencies**

Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### **4. Run the Application

Once your API key is set up and dependencies are installed, you can run the application:

```bash
python pp.py
```
