# ==========================================
# Trying to build a good streamlit dashboard
# ==========================================


import pandas as pd
import streamlit as st
import os
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


# Load in data
df = pd.read_csv(r".\data\dashboard_data.csv")


# For text

pos_sent = df[df["sentiment"] == "LABEL_1"]
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
full_pos = " ".join(pos_sent["review_text"].astype(str)).lower()
# Remove stopwords
cor_pos = " ".join(word for word in full_pos.split() if word not in stop_words)


neg_sent = df[df["sentiment"] == "LABEL_0"]
full_neg = " ".join(neg_sent["review_text"].astype(str)).lower()
#remove stop words
cor_neg = " ".join(word for word in full_neg.split() if word not in stop_words)

#
# Dashboard title

st.title("Marriott Hotels Google Maps 2026 Customer Reviews Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("**Positive Reviews**", len(pos_sent))

    st.write("Common Words in Positive Reviews")
    wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white'
    ).generate(cor_pos)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    if st.button("View Positive Reviews Details"):
        st.session_state.view = "positive"


with col2:
    st.metric("**Negative Reviews**", len(neg_sent))

    st.write("Common Words in Negative Reviews")
    wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white'
    ).generate(cor_neg)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    if st.button("View Negative Review Details"):
        st.session_state.view = "negative"

if st.session_state.get("view") == "positive":
    st.subheader("Positive Review details")

    # I need to plot countplot of the different positive review types

    fig, ax = plt.subplots()
    sns.countplot(data=pos_sent, x='category', ax=ax)
    ax.set_title("Count of Review Category")
    st.pyplot(fig)

    st.subheader("Top 5 Positive Reviews")
    reviews = pos_sent["review_text"].tail(5).to_list()
    for i, review in enumerate(reviews, start=1):
        st.success(f"{i}. {review}")
if st.session_state.get("view") == "negative":
    st.subheader("Negative Review details")

    # I need to plot countplot of the different positive review types

    fig, ax = plt.subplots()
    sns.countplot(data=neg_sent, x='category', ax=ax)
    ax.set_title("Count of Review Category")
    st.pyplot(fig)

    st.subheader("Top 5 Negative Reviews")
    reviews = neg_sent["review_text"].head(5).to_list()
    for i, review in enumerate(reviews, start=1):
        st.warning(f"{i}. {review}")
