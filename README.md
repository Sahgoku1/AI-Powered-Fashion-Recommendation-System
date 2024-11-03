# AI-Powered Fashion Recommendation System

**_Project Overview_**
This project presents a recommendation system designed for the fashion industry, targeting both luxury and retail segments. The system leverages generative AI and machine learning to convert unstructured fashion data into structured insights, facilitating product recommendations, brand classification, and style analysis.

**_Motivation_**

The fashion industry is driven by continuous trend changes and customer demands, with luxury and retail brands often overlapping in style influences. By structuring data and enabling cross-brand analysis, this project empowers brands and consumers to explore stylistic similarities and alternative products.

**_Methodology_**

**Data Collection and Structuring**

Data Scraping: Collected product data from selected luxury and retail brands, including images, text descriptions, and metadata.
Large Language Models (LLMs): LLMs structured the data by generating detailed descriptions and identifying product characteristics.
Feature Engineering: Converted product features into embeddings, capturing semantic similarities for recommendation and classification.

**Recommendation System Development**

The recommendation model supports:
1. Luxury to Retail Recommendations: Identifies retail items with stylistic similarities to luxury products.
2. Text-Based Recommendations: Matches products to user-provided descriptions.
3. Image-Based Recommendations: Recommends items based on uploaded reference images.
   
**Classification and Similarity Analysis**
- Brand Classification: Used RandomForestClassifier and Recursive Feature Elimination to distinguish between luxury and retail brands.
- Semantic Clustering: Applied cosine similarity and hierarchical clustering for style-based analysis across brands.

**_Tech Stack_**
Language: Python
Machine Learning: Scikit-learn, Pre-trained Embedding Models
Database: PostgreSQL for structured data, ChromaDB for embedding storage
Environment: Docker for scalability and deployment

**_Main Features_**

1. Cross-Brand Recommendations: Uses embeddings to match products with similar style attributes.
2. Style Classification: Differentiates brand tiers and identifies unique style patterns.
3. Automated Data Structuring: AI-driven analysis of product features for consistency and comparability.

