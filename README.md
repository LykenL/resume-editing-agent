# Resume Optimization Agent

A local-first, AI-powered tool that automatically optimizes your resume (DOCX format) against a specific Job Description (JD) to maximize ATS (Applicant Tracking System) matching. It uses a two-stage pipeline: a lightweight local model for fast intelligence extraction, and a more capable model for high-quality, ATS-optimized rewrites.

## Prerequisites

Before running or deploying the application, ensure you have the following installed:

1. **Python 3.10+**
2. **Ollama**: A local LLM runner. You must have it installed and running on your machine.
3. **Required AI Models**: Pull the required models via Ollama. By default, the app uses `qwen3.5:4b` for extraction and `gpt-oss:20b-cloud` for the evaluator rewrite. You can customize these in `app.py`.
   ```bash
   ollama pull qwen3.5:4b
   ollama pull gpt-oss:20b-cloud
   ```
4. **Ngrok** (Optional, for Cloud Deployment): If you plan to deploy the app on Streamlit Cloud but want to use your local Ollama models, you need Ngrok to expose your local port.

## Local Deployment

To run the application entirely on your local machine:

1. **Clone the repository and install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Ollama**:
   Ensure Ollama is running in the background. If not, open a terminal and run:
   ```bash
   ollama serve
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```
   The application will be accessible at `http://localhost:8501`.

## Cloud Deployment (Streamlit Cloud)

If you wish to deploy the frontend to Streamlit Cloud while keeping your data and models secure on your local machine:

1. **Deploy to Streamlit Cloud**:
   - Connect your GitHub repository to Streamlit Community Cloud.
   - Point the main file path to `app.py`.
   - Streamlit will automatically install dependencies from `requirements.txt`.

2. **Expose Local Ollama via Ngrok**:
   - Since the cloud app cannot reach your `localhost`, run Ngrok on your machine:
     ```bash
     ngrok http 11434
     ```
   - Copy the forwarding URL provided by Ngrok (e.g., `https://xxxx.ngrok-free.app`).

3. **Configure the App**:
   - Open your deployed Streamlit app.
   - In the sidebar, locate the "Ollama Server URL" input box.
   - Paste your Ngrok forwarding URL into the box.
   - The app will now communicate with your local machine's AI models.

## Usage Guide

1. Upload your existing resume in `.docx` format.
2. Provide a Job Description either by pasting the URL (LinkedIn, Greenhouse, etc.) or pasting the raw text.
3. Click "Optimize My Resume".
4. The app will generate a tailored version of your resume, preserving formatting and strictly matching the target JD's keywords.
5. Download the final `.docx` file or revisit past runs from the sidebar history.
