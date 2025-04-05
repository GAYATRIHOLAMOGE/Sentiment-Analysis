Instagram Sentiment Analysis

Overview

This project extracts comments from Instagram posts using Instaloader, processes them, and performs sentiment analysis. The goal is to analyze user sentiment on Instagram posts by scraping comments and filtering out those containing emojis before analysis.

Features

Extracts comments from an Instagram post.

Uses cookies from a Firefox browser session for authentication.

Filters out comments containing emojis.

Saves comments to a text file for further processing.

Performs sentiment analysis on the extracted comments.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.7+

Instaloader (pip install instaloader)

SQLite3 (default in Python)

Required sentiment analysis libraries (NLTK, TextBlob, or any other specified in your Sentiment analysis code.ipynb)

Setup

Clone or download this repository:

git clone https://github.com/YOUR_GITHUB_USERNAME/Instagram-Sentiment-Analysis.git
cd Instagram-Sentiment-Analysis

Install dependencies:

pip install -r requirements.txt

Modify sentimentscraper.py:

Set output_file_path to define where to save comments.

Set path_to_firefox_cookies to the path of your cookies.sqlite file.

Replace USERNAME with your Instagram username.

Replace SHORTCODE with the shortcode of the Instagram post you want to analyze.

Usage

Step 1: Scraping Comments

Run sentimentscraper.py to extract comments from an Instagram post.

python sentimentscraper.py

This will:

Authenticate using browser cookies.

Extract up to 1000 comments.

Save them to the specified output file.

Step 2: Sentiment Analysis

Use Sentiment analysis code.ipynb to:

Load the extracted comments.

Process them for sentiment classification (positive, neutral, negative).

Display or save results for further interpretation.

Notes

Ensure you have logged into Instagram via Firefox before running the script to use session cookies.

Instagram rate limits may apply, so keep a delay between requests.

Sentiment analysis may require additional data preprocessing for better accuracy.
