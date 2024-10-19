![image](https://github.com/user-attachments/assets/dc827a8f-2921-43e9-8d24-dc5edca1679f)

## AI-Powered Database Query Chatbot: Effortless Data Access and Insights

### **Table of Contents**

1. [Project Overview](#overview)
2. [Key Features](#key-features)
3. [Tools & Technologies](#tools--technologies)
4. [Folder Structure](#folder-structure)
5. [Installation Guide](#installation-guide)
6. [Usage Instructions](#usage-instructions)
7. [Contribution Guidelines](#contribution-guidelines)
8. [Conclusion](#conclusion)


---

### Overview
The **AI Database Chatbot** is an innovative project designed to transform users' interactions with relational databases. At its core, this chatbot is powered by advanced AI models from OpenAI, enabling it to understand and respond to natural language queries about data stored in a Postgres database. This project was built to simplify data retrieval processes, allowing users to access and understand complex database information effortlessly regardless of their technical background.

Traditionally, extracting insights from databases required proficiency in SQL or other querying languages. The **AI Database Chatbot** eliminates this barrier by providing a conversational interface where users can ask questions in plain English. Whether you’re a business analyst needing quick data insights or a developer testing database queries, this chatbot offers a user-friendly platform to interact with your data. The integration with Streamlit further enhances the user experience, delivering a clean, responsive, and interactive web application that can be easily deployed and accessed from any browser.


---

### Key Features

- **Interactive User Interface:** The chatbot provides a seamless and engaging user experience through a web-based interface developed with Streamlit. This interface is designed to be intuitive and user-friendly, allowing users to interact with the chatbot effortlessly. The UI supports various themes and is customizable to suit different user preferences.

- **AI-Powered Responses:** The core of the chatbot's functionality is powered by OpenAI's advanced language models. These models are trained to understand and generate human-like responses, ensuring that users receive accurate, contextually relevant answers to their queries. The AI's natural language processing capabilities enable it to handle complex questions and provide meaningful insights.

- **Database Integration:** The chatbot is integrated with a Postgres relational database, allowing it to access and retrieve real-time data. This integration ensures that the information provided is current and reflects any updates or changes made to the database. The chatbot can perform sophisticated queries to extract and present data based on user input.

- **Conversation History:** To enhance user experience and provide a record of interactions, the chatbot saves conversation history in markdown format. This feature allows users to review past interactions, track queries, and analyze responses. The markdown format ensures that the saved conversations are easily readable and can be used for future reference or documentation.

---

### **Tools & Technologies**

| **Tool**      | **Purpose**                                                   | **Details**                                                                                               |
|---------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Streamlit** | Creates an interactive and user-friendly web-based interface. | Streamlit is a Python library that enables rapid development of web applications with minimal code. It is used here to build the chatbot’s front-end, providing an interactive and visually appealing user experience. |
| **OpenAI**    | Powers the chatbot’s intelligent and contextual responses.    | OpenAI’s models, such as GPT-4, are employed to generate responses based on user queries. These models are renowned for their ability to understand context and provide accurate, coherent answers. |
| **Postgres**  | Hosts the relational database containing the core data.       | PostgreSQL is a powerful open-source relational database system used to store and manage the data accessed by the chatbot. It supports complex queries and transactions, ensuring reliable data management and retrieval. |

---


### **Folder Structure**
The project is organized as follows:

```plaintext
│   .env
│   .gitignore
│   app.py
│   README.md
│   requirements.txt
│
├───assets
│   │   dark_theme.py
│   │   light_theme.py
│   │   made_by_sdw.py
│   │
│   └───__pycache__
│           ...
│
├───chatlogs
│       ...
│
└───utils
    │   api_functions.py
    │   chat_functions.py
    │   config.py
    │   database_functions.py
    │   function_calling_spec.py
    │   helper_functions.py
    │   system_prompts.py
    │
    └───__pycache__
            ...
```

---

### **Installation Guide**
Follow these steps to set up and run the AI Database Chatbot on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/AI-Powered-Database-Query-Chatbot.git
   cd AI-Powered Database Query Chatbot
   ```

2. **Install Required Packages:**
   Use the following command to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   - Add your database credentials and OpenAI API key in the `.env` file.

---

### **Usage Instructions**
After completing the installation, follow these steps to run the chatbot:

1. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Interacting with the Chatbot:**
   - Upon running the application, the chatbot interface will automatically open in your default web browser.
   - You can begin by entering your queries related to the database directly into the chat interface. The chatbot will generate intelligent and well-structured responses based on your input.
   - Additionally, you have the option to save your interactions as markdown files, allowing you to review and reference previous conversations at your convenience.

---




### **Contribution Guidelines**

We welcome contributions from the community! Whether it's enhancing features, fixing bugs, or providing feedback, your involvement is valuable. To contribute, please follow these steps:

1. **Fork the Repository:** Click the "Fork" button at the top right of this repository to create your copy.
2. **Create a New Branch:** From your forked repository, create a new branch for your feature or bug fix. Ensure your branch name is descriptive.
3. **Submit a Pull Request:** After committing your changes to your branch, submit a pull request to the main repository. Provide a detailed description of your changes and the purpose of your pull request.

---

### **Conclusion**
In today's data-driven world, accessing and interpreting vast amounts of information stored in databases can be challenging, particularly for those who are not well-versed in querying languages. The **AI Database Chatbot** was created to bridge this gap by providing an intuitive, AI-powered interface that allows users to interact with their data naturally and efficiently. By integrating advanced AI models with a robust database system like Postgres, we’ve developed a solution that democratizes data access, making it easier for users to extract meaningful insights without the need for deep technical expertise.

This project has successfully demonstrated how AI can be harnessed to enhance data accessibility and user engagement. From setting up a seamless interface to ensuring accurate and context-aware responses, the **AI Database Chatbot** embodies the potential of modern technology in transforming how we interact with and understand data. This tool not only simplifies database querying but also paves the way for more innovative applications in AI-driven data analysis.

---


### Connect With Me 

**[![LinkedIn](https://img.shields.io/badge/LinkedIn-Viraj%20Bhutada-blue?logo=linkedin)](https://www.linkedin.com/in/virajnbhutada24/) [![GitHub](https://img.shields.io/badge/GitHub-Viraj%20Bhutada-2b3137?logo=github)](https://github.com/virajbhutada)**

