## Project Title

**Whatsapp Chat Analyzer**

## Overview

- A Streamlit-based web application to analyze WhatsApp chat data. This tool helps users visualize chat statistics such as total messages, words, media shared, and links. It also allows users to explore monthly chat trends and identify the most active users.

## Project Overview
This project provides a comprehensive analysis of WhatsApp chat data. It uses:

- Python for backend processing,
- Streamlit for the frontend, and
- Pandas for data processing.

The app allows users to upload a chat file, view user activity, and track media and link sharing in their WhatsApp group chats.

## Data Overview

- Data Source: WhatsApp chat export (text file).
- Key Columns: user, message, date, year, month_num, month, day, etc.
- Dataset: Includes WhatsApp chat messages with timestamps, user names, and media or link data.

## Chat Analysis Workflow
- **Data Preprocessing:** Parses and structures the chat messages with timestamps and user information.
- **User Stats:** Displays the total number of messages, words, media shared, and links for selected users.
- **Monthly Trends:** Visualizes message activity over time for selected users.
- **Most Active Users:** Identifies and ranks the users based on message count.

## Key Features

- **User Statistics:** View total messages, words, media shared, and links for selected users.
- **Timeline Visualization:** Monthly trends of message frequency.
- **Most Active Users:** Identifies the most active users in the chat.
- **Interactive Web Interface:** User-friendly and intuitive, built using Streamlit.
- **File Upload:** Upload WhatsApp chat files for analysis.

# Technologies Used

- Languages: Python
- Libraries: Pandas, Matplotlib, Streamlit, URLExtract
- Data Processing: Regex for message parsing, Pandas for data manipulation
- Frontend: Streamlit for creating the user interface

# Demo
Here’s a quick demonstration of the application:

Screenshots:


## Features

- **Show User Stats:** Displays statistics related to messages, words, media, and links for a specific user.
- **Timeline Visualization:** Monthly trends of message counts for better understanding of chat dynamics.
- **Most Active Users:** Helps identify the most active users in the chat.
- **Interactive Interface:** Built with Streamlit for ease of use.
- **File Upload:** Upload your WhatsApp chat file for analysis.

## Usage

- **Launch the Application:** Open the app in a web browser using the provided URL.
- **Upload a WhatsApp Chat File:** Upload a WhatsApp exported chat file from your device.
- **Select a User:** Choose a user from the sidebar to view their chat statistics.
- **View Analysis:** Click on "Show Analysis" to view the statistics, timeline, and activity of the selected user.

## File Descriptions
- **app.py:** The main Streamlit application script that loads the data, computes chat statistics, and renders the user interface.
- **preprocessor.py:** Handles the preprocessing of WhatsApp chat data, including parsing and cleaning.
- **helper.py:** Contains helper functions to calculate user statistics, generate timelines, and determine the most active users.
- **requirements.txt:** Lists all the required Python packages for running the application.

## Conclusion

This Whatsapp Chat Analyzer provides users with insightful analysis of their WhatsApp chat data. By analyzing key metrics like message count, word usage, and media sharing, users can gain valuable insights into their chat activity. With an intuitive interface built with Streamlit, this tool is easy to use and deployable on any local system.
With further improvements, the tool could include more advanced features like sentiment analysis or automated summaries, making it even more useful for users to explore and understand their chat data better.
