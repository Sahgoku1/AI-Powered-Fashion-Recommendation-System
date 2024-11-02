# Fashion Recommendation System for Luxury and Retail Brands

**_Project Overview_**

This project focuses on creating an AI-powered recommendation system for the fashion industry, bridging the gap between luxury and retail segments. By leveraging generative AI and machine learning, we transformed unstructured data into actionable insights to support stylistic comparisons, product recommendations, and brand classification.

**_Motivation_**

The fashion industry produces vast amounts of unstructured data, making it challenging to derive consistent insights into trends and styles. This project introduces an end-to-end framework to structure this data, providing useful recommendations for consumers and analytical tools for brands.

**_Methodology_**

**Data Collection & Structuring**

1. Data Scraping: Collected product data from multiple luxury and retail brands.
2. Large Language Models (LLMs): Used LLMs to generate structured product descriptions.
3. Feature Engineering: Created embeddings for semantic representation of style attributes.
 
**Recommendation System Development**

Our recommendation system includes:
Luxury to Retail Recommendations: Find retail items similar to luxury fashion.
Text-to-Product Recommendations: Recommends items based on textual descriptions.
Image-to-Product Recommendations: Suggest items similar to an uploaded image.

Classification & Similarity Analysis:
Classification: A RandomForestClassifier with Recursive Feature Elimination (RFE) differentiates between brands.
Semantic Similarity: Uses cosine similarity and hierarchical clustering to identify stylistic relationships.

**Tech Stack** 
Languages: Python
Machine Learning: Scikit-learn, Embedding Models
Database: PostgreSQL, ChromaDB for embedding storage
Environment: Docker for scalability and portability

**_Main Features_**

Feature-Rich Recommendations: Text and image-based recommendations for seamless user experiences.
AI-Powered Data Structuring: Automatic extraction and organization of product characteristics.
Brand Classification: Distinguishes luxury from retail brands with high accuracy.
