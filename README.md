# fintech-review-analysis
The Third Week's Challange on my Jorney into Kifya X 10Acadamy DS Bootcamp 

This project collects and analyzes customer reviews for mobile banking apps of Ethiopian banks: CBE, BOA, and Dashen.

## ✅ Completed Tasks (Interim - June 8)

### Task 1: Scraping & Preprocessing
- Used `google-play-scraper` to scrape 400+ reviews per bank (1200+ total)
- Preprocessed data: removed duplicates, normalized dates

### Task 2 (Partial): Sentiment Analysis
- Applied VADER on 400 reviews from CBE
- Added `sentiment_score` and `sentiment_label`

## 📁 Structure

- `scripts/`: All scripts for scraping, cleaning, analysis
- `data/`: CSVs for raw, cleaned, and sentiment results
- `README.md`, `.gitignore`, `requirements.txt`

## 🚀 How to Run

```bash
pip install -r requirements.txt
python scripts/scrape_reviews.py
python scripts/preprocess_reviews.py
python scripts/sentiment_analysis.py
```