# ML Experiment Dashboard

A full-stack machine learning experiment dashboard for training, tracking, and comparing model performance across datasets.

This project demonstrates backend API design, experiment tracking, data visualization, and lightweight ML pipelines.

## Features

- Train ML models on tabular datasets
- Store experiment results in database
- Compare model performance
- Interactive dashboard
- Fast training using scikit-learn
- Full-stack architecture

## Tech Stack

Backend:
- Python
- FastAPI
- SQLite
- scikit-learn
- pandas

Frontend:
- React / Next.js
- Chart.js

ML:
- Linear Regression
- Decision Tree
- Random Forest

Tools:
- Git
- GitHub
- VSCode

## Project Structure

```
ml-experiment-dashboard/
  backend/
  frontend/
  notebooks/
  data/
  README.md
```

## How to run backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## How to run frontend

```
cd frontend
npm install
npm run dev
```

## Goals of this project

- Demonstrate full-stack ML system
- Show experiment tracking workflow
- Build production-style project
- Practice backend + frontend + ML integration

## Future Improvements

- Add user login
- Add more datasets
- Add hyperparameter tuning
- Deploy online
- Add experiment filters
