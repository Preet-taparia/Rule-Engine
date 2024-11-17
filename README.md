# **Security Rule Engine**

The **Security Rule Engine** is a system designed to enhance network security by managing and monitoring network access policies. It consists of two main components:  
1. **Rule Engine Application** (installed on users' computers): Captures and analyzes network packets in real time, enforcing security rules.  
2. **Central Web Console** (accessible by admins): Provides a centralized interface for managing rules, monitoring logs, and receiving alerts.

---

## **Table of Contents**
1. [Tech Stack](#tech-stack)
2. [Features](#features)
3. [Architecture Overview](#architecture-overview)
4. [Installation](#installation)
   - [Rule Engine Application](#rule-engine-application)
   - [Central Web Console](#central-web-console)
5. [Usage](#usage)
6. [API Reference](#api-reference)
7. [Contributing](#contributing)
8. [License](#license)

---

## **Tech Stack**

### **Rule Engine Application**
- **Python**: Core programming language.
- **Libraries**:
  - **Pyshark**: For real-time packet capturing and analysis.
  - **Requests**: Handles HTTP communication with the Central Web Console.
  - **Socket.IO**: Enables real-time communication with the Central Web Console.

### **Central Web Console**
- **Node.js and Express**: Backend server framework for managing APIs and socket connections.
- **React**: Frontend library for building dynamic, interactive user interfaces.
- **Socket.IO**: Provides real-time updates and notifications.

---

## **Features**
- **Packet Capturing**: Captures and inspects network packets in real time.
- **Rule Management**: Add, edit, or delete security rules via the web console.
- **Real-Time Alerts**: Notifies admins about suspicious activities or rule violations.
- **Log Monitoring**: Centralized view of network activity logs.
- **Customizable Policies**: Easily configure and deploy network access policies.

---

## **Architecture Overview**
### **Workflow**
1. **Rule Engine Application**:
   - Captures packets using Pyshark.
   - Processes and enforces rules locally.
   - Sends logs to the Central Web Console.

2. **Central Web Console**:
   - Serves as a management platform for rules and logs.
   - Sends updated rules to the Rule Engine in real time.

### **Component Interaction Diagram**
```plaintext
+-----------------+       +---------------------------+
| Rule Engine App | <---> | Central Web Console       |
| (Pyshark, Flask)|       | (Node.js, React, SocketIO)|
+-----------------+       +---------------------------+
```

---

## **Installation**

### **Prerequisites**
- **Python 3.8+**
- **Node.js 16+**
- **npm (Node Package Manager)**

### **Rule Engine Application**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the Rule Engine directory:
   ```bash
   cd rule-engine-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

### **Central Web Console**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the Central Web Console directory:
   ```bash
   cd central-web-console
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the backend server:
   ```bash
   npm start
   ```
5. Start the frontend development server:
   ```bash
   npm run start-client
   ```

---

## **Usage**

### **Rule Engine Application**
- Monitors network activity and enforces rules defined by the Central Web Console.
- Stores and sends logs to the console in real time.

### **Central Web Console**
#### **Adding Rules**
1. Log in as an admin.
2. Navigate to the "Rules" tab.
3. Click **Add Rule**, fill out the necessary fields, and save.

#### **Viewing Logs**
- Navigate to the "Logs" tab to view captured network activity in real time.

#### **Real-Time Alerts**
- View alerts for suspicious activities directly on the dashboard.

---

## **API Reference**
### **Rule Management**
- **GET `/api/rules`**  
  Fetch all security rules.
  
  **Response**:
  ```json
  [
    {
      "id": 1,
      "source_ip": "192.168.1.1",
      "destination_ip": "10.0.0.1",
      "action": "ALLOW"
    },
    {
      "id": 2,
      "source_ip": "192.168.1.2",
      "action": "DENY"
    }
  ]
  ```

- **POST `/api/rules`**  
  Add a new security rule.

  **Request Body**:
  ```json
  {
    "source_ip": "192.168.1.100",
    "action": "ALLOW"
  }
  ```

- **DELETE `/api/rules/<id>`**  
  Delete a specific rule by ID.

---

## **Contributing**

We welcome contributions to improve the Security Rule Engine. Here's how you can get involved:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

Feel free to update this document as the project evolves or if new features are added!