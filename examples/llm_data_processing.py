"""
Example: Processing LLM data with Pandas
"""

import pandas as pd

def process_llm_responses(df: pd.DataFrame):
    """Process LLM responses in DataFrame"""
    df['response_length'] = df['response'].str.len()
    df['word_count'] = df['response'].str.split().str.len()
    df['has_code'] = df['response'].str.contains('```', regex=False)
    return df

# Usage
# df = pd.DataFrame({
#     'prompt': ['What is AI?', 'Explain ML'],
#     'response': ['AI is...', 'ML is...']
# })
# processed = process_llm_responses(df)

