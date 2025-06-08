import pandas as pd
from google_play_scraper import reviews, Sort
import logging

BANK_APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

RAW_DATA_PATH = "data/reviews_raw.csv"
CLEANED_DATA_PATH = "data/reviews_cleaned.csv"
SENTIMENT_SAMPLE_PATH = "data/sentiment_sample.csv"

logging.basicConfig(level=logging.INFO)

def scrape_reviews_per_bank(count: int = 400) -> pd.DataFrame:
    """Scrapes reviews for defined banks from Google Play Store."""
    all_reviews = []

    for bank, app_id in BANK_APPS.items():
        logging.info(f"Scraping {count} reviews for {bank}")
        results, _ = reviews(
            app_id,
            lang='en',
            country='us',
            count=count,
            sort=Sort.NEWEST
        )
        print(f"Found {len(results)} reviews for {bank}")
        if not results:
            logging.warning(f"No reviews found for {bank}")
            continue
        for r in results:
            all_reviews.append({
                "review": r["content"],
                "rating": r["score"],
                "date": r["at"].strftime("%Y-%m-%d"),
                "bank": bank,
                "source": "Google Play"
            })

    df = pd.DataFrame(all_reviews)
    df.to_csv(RAW_DATA_PATH, index=False)
    logging.info(f"Saved {len(df)} raw reviews to {RAW_DATA_PATH}")
    return df

def clean_reviews() -> pd.DataFrame:
    """Cleans the scraped reviews dataset."""
    df = pd.read_csv(RAW_DATA_PATH)

    initial = len(df)
    df.drop_duplicates(subset="review", inplace=True)
    df.dropna(subset=["review"], inplace=True)
    df = df.loc[:, ["review", "rating", "date", "bank", "source"]]
    if isinstance(df, pd.Series):
        df = df.to_frame().T

    df.to_csv(CLEANED_DATA_PATH, index=False)
    logging.info(f"Cleaned {initial} ➜ {len(df)} reviews. Saved to {CLEANED_DATA_PATH}")
    return df
