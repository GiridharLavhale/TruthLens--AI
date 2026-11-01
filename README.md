# TruthLens-AI 🔍
### AI-Powered Real-Time Misinformation Detection System

TruthLens-AI is an AI-powered misinformation detection application designed to analyze video content and help identify potentially misleading information.

The project combines a Python-based backend with a React frontend to provide video analysis, transcription, OCR-based text extraction, classification, keyword checking, deepfake detection components, and analysis reporting.

---

## 📌 Project Overview

The rapid growth of digital media has made it increasingly difficult to distinguish trustworthy information from misinformation.

TruthLens-AI aims to help users examine video content through multiple AI-based analysis components and present the results through an interactive dashboard.

The application provides a platform for analyzing video content and reviewing the generated analysis.

---

## ✨ Features

- **Video Upload:** Upload video files for analysis.
- **Audio Extraction:** Extract audio from uploaded videos using FFmpeg.
- **Speech-to-Text:** Transcribe extracted audio using speech recognition technology.
- **OCR Text Extraction:** Extract visible text from video content.
- **Misinformation Classification:** Analyze content using a trained machine-learning model.
- **Keyword Analysis:** Check content for relevant keywords.
- **Deepfake Detection Component:** Includes a deepfake detection service.
- **Category Detection:** Identify content categories.
- **AI-Based Explanations:** Generate explanations for analysis results.
- **Analysis History:** Retrieve previously analyzed videos.
- **PDF Reports:** Generate downloadable analysis reports.
- **Interactive Dashboard:** View analysis information through a React-based interface.

---

## 🛠️ Technologies Used

### Backend
- Python 3.11
- FastAPI
- Uvicorn
- PyTorch
- Scikit-learn
- OpenCV
- EasyOCR
- Faster-Whisper
- OpenAI Whisper
- SQLite
- ReportLab
- FFmpeg

### Frontend
- React 19
- Vite
- JavaScript
- HTML5
- CSS3
- Axios
- Recharts
- Tailwind CSS
- Shadcn/UI components

### Machine Learning
- Scikit-learn
- PyTorch
- Machine-learning model files (`.pkl`)
- Text preprocessing
- Classification and vectorization

---

## 📂 Project Structure

```text
TruthLens-AI/
│
├── app/
│   ├── database/
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── fake_news_model.pkl
│   │   └── vectorizer.pkl
│   │
│   ├── routes/
│   │   └── upload.py
│   │
│   ├── services/
│   │   ├── audio_extractor.py
│   │   ├── category_detector.py
│   │   ├── classifier.py
│   │   ├── deepfake_detector.py
│   │   ├── explainer.py
│   │   ├── keyword_checker.py
│   │   ├── ocr_extractor.py
│   │   ├── preprocessing.py
│   │   ├── report_generator.py
│   │   └── transcriber.py
│   │
│   └── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── train_model.py
├── requirements.txt
├── requirements-local.txt
├── render.yaml
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

Follow these steps to run TruthLens-AI locally.

### 1. Prerequisites

Install the following software:

- Python 3.11
- Node.js and npm
- Git
- FFmpeg
- Visual Studio Code (recommended)

### 2. Clone the Repository

```bash
git clone https://github.com/GiridharLavhale/TruthLens--AI.git
```

Navigate into the project:

```bash
cd TruthLens-AI
```

### 3. Set Up the Python Backend

Create a virtual environment:

```bash
py -3.11 -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the locally compatible dependencies:

```bash
python -m pip install -r requirements-local.txt
```

**Note:** `requirements-local.txt` contains the dependency adjustments used for the tested Python 3.11 Windows setup. The original `requirements.txt` is also included in the repository.

### 4. Install FFmpeg

FFmpeg is required for audio extraction from uploaded videos.

On Windows, you can install it using:

```powershell
winget install --id Gyan.FFmpeg --exact
```

Restart your terminal after installation.

Verify FFmpeg:

```powershell
ffmpeg -version
```

If Windows cannot find FFmpeg, add its installation `bin` directory to your system PATH.

### 5. Start the Backend Server

From the root project directory, with the virtual environment activated:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend server:

```text
http://127.0.0.1:8000
```

FastAPI interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Set Up the Frontend

Open a second terminal:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the frontend development server:

```bash
npm run dev
```

Frontend application:

```text
http://localhost:5173
```

---

## 🚀 Running the Complete Application

You need two separate terminals.

**Terminal 1 – Backend**

```powershell
cd C:\Users\ASUS\Desktop\TruthLens-AI

.\venv\Scripts\Activate.ps1

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Terminal 2 – Frontend**

```powershell
cd C:\Users\ASUS\Desktop\TruthLens-AI\frontend

npm run dev
```

Open your browser:

```text
http://localhost:5173
```

---

## 🔗 API Endpoints

The backend provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check backend status |
| POST | `/analyze-video` | Upload and analyze a video |
| GET | `/history` | Retrieve video analysis history |
| GET | `/generate-report/{video_id}` | Generate an analysis report |

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 🧠 Machine Learning Models

The project includes the following model files:

- `fake_news_model.pkl` – Trained classification model.
- `vectorizer.pkl` – Text vectorization model.

These files are located inside:

```text
app/models/
```

The project also includes:

```text
train_model.py
```

for model training.

---

## 🗄️ Database

TruthLens-AI uses SQLite for storing video analysis information.

The database configuration is available in:

```text
app/database/db.py
```

---

## 📊 Application Workflow

1. User opens the TruthLens-AI frontend.
2. User uploads a video.
3. Backend receives the uploaded video.
4. FFmpeg extracts audio from the video.
5. Speech transcription and OCR processing are performed by the relevant services.
6. Classification, keyword analysis, and other analysis components are invoked.
7. Analysis results are returned to the frontend.
8. The user can view analysis history and generate a PDF report.

---

## 🔒 Important Notes

- Keep API keys and passwords out of public repositories.
- Do not upload `.env` files or other confidential information.
- FFmpeg must be installed and accessible through PATH.
- Machine-learning model files are included in the repository.
- Some AI processing tasks may require additional time and system resources.
- CPU-based processing may be slower than GPU-based processing.
- AI-generated classifications should be treated as assistance, not as definitive proof that content is true or false.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Improved misinformation classification accuracy.
- Advanced deepfake detection.
- More language support for speech transcription.
- Real-time video analysis.
- Improved explanation and evidence presentation.
- Enhanced model evaluation and performance.
- Cloud deployment and scalability improvements.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes.
5. Submit a pull request.

---

## 👨‍💻 Author

**Giridhar Lavhale**

GitHub: https://github.com/GiridharLavhale

Project: [TruthLens-AI](https://github.com/GiridharLavhale/TruthLens--AI)

---

## 📜 License

No license has been specified yet. All rights are reserved by the project author unless a license is added to this repository.

---

**TruthLens-AI – Making digital information easier to examine.** 🔍