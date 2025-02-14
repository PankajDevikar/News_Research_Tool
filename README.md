# News Research Tool

## Project Overview
The News Research Tool is a Streamlit-based web application that fetches and displays the latest news articles relevant to a given query. It leverages the NewsAPI to retrieve news articles and allows users to customize the model settings via Groq's LLM models.

## Features
- Fetch latest news articles based on user query
- Display article titles, descriptions, and links
- Sidebar settings for Groq API model selection and tuning parameters
- Interactive user input for dynamic news retrieval

## Project Pipeline
1. **User Input**: The user provides a query for relevant news articles.
2. **Fetch News**: The NewsAPI fetches relevant articles based on the query.
3. **Process Data**: Extracts key details like title, description, and URL.
4. **Display Results**: News articles are displayed in the Streamlit interface.
5. **Image Display**: Outputs an image for better visualization.

## Installation
1. Clone the repository:
   ```bash
   git clone (https://github.com/PankajDevikar/News_Research_Tool.git)

   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add:
   - 
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Integrate AI-powered news summarization.
- Implement sentiment analysis on articles.
- Add real-time notifications for breaking news.

## Output Display
![Main UI](https://github.com/PankajDevikar/News_Research_Tool/blob/main/img2.png)
![Summary](https://github.com/PankajDevikar/News_Research_Tool/blob/main/img3.png)

