**TrustNetAI – AI-Based Phishing Detection System**

* **Description:** Web application developed for the automatic identification of phishing attempts through the intelligent analysis of email streams.
* **Technologies:** Python, Flask, OpenAI API (GPT-3.5-Turbo), IMAP, HTML.
* **Key Features:**
* Implementation of a secure connection module for email servers (e.g., Outlook/Office 365) using the IMAP protocol for real-time message retrieval.
* Integration of Large Language Models (LLMs) via the OpenAI API to evaluate the subject, sender, and content of emails, generating a security verdict and a confidence score.
* Development of an intuitive web interface using the Flask framework, which allows for the triggering of AI analyses through a single interaction.
* Processing of complex email structures (multipart), including header decoding and automatic attachment management by saving them in dedicated directories for further analysis.


* **Impact:** Automates the sorting of suspicious messages, providing an additional layer of cybersecurity by utilizing natural language processing to detect fraud indicators.
