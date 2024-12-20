# Alignment Score Calculation Instructions

## Overview
This document outlines the method for calculating an alignment score between two sets of information, such as comparing brand guidelines to a social media post. The alignment score quantifies the consistency of the content of the post with the established guidelines.

## Score Calculation
The alignment score is derived by analyzing the similarity in themes, keywords, tone, and style between the two texts. This involves several steps:

### Step 1: Text Preprocessing
- **Objective**: Clean and standardize the text format.
- **Actions**: Remove noise such as special characters and normalize text formats (e.g., lowercasing).

### Step 2: Keyword Extraction
- **Objective**: Identify key terms that represent the core topics.
- **Actions**: Use Natural Language Processing (NLP) techniques like TF-IDF or topic modeling to extract significant keywords.

### Step 3: Semantic Analysis
- **Objective**: Understand the contextual meanings of the texts.
- **Actions**: Apply semantic analysis tools to interpret the context behind the keywords and phrases.

### Step 4: Data Comparison
- **Objective**: Assess the similarity between the two processed datasets.
- **Actions**: Use cosine similarity or another statistical measure to compare the semantic representations of both texts.

### Step 5: Scoring
- **Objective**: Quantify the alignment.
- **Actions**: Calculate the final score as a percentage where 100% represents perfect alignment.

## Use Cases
The alignment score is particularly useful for:
- Ensuring consistency across marketing materials.
- Evaluating how well advertising campaigns align with brand guidelines.
- Integrating into content management systems to maintain brand coherence.

## Return Format
The alignment score should be communicated in a structured format, such as JSON, with the following elements:

```json
{
  "alignment_score": 85.6,
  "details": {
    "themes": 90,
    "keywords": 80,
    "tone": 85,
    "style": 90
  }
}
```

!!! IMPORTANT MAKE SURE TO MAINTAIN ```json{valid_json}``` FORMAT AND STRUCTURE WHEN COMMUNICATING. !!!