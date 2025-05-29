import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

#Step 1: Read Dataset ---
try:
    dataset = pd.read_csv('sample_data.csv')
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# --- Step 2: Split Features and Target ---
input_data = dataset.drop('target', axis=1)
output_labels = dataset['target']

#  Step 3: Column Type Identification 
num_cols = ['age', 'salary']
cat_cols = ['department', 'city']

# Step 4: Create Preprocessing Pipelines ---
num_processor = Pipeline(steps=[
    ('fill_missing', SimpleImputer(strategy='mean')),
    ('normalize', StandardScaler())
])

cat_processor = Pipeline(steps=[
    ('fill_mode', SimpleImputer(strategy='most_frequent')),
    ('encode', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# --- Step 5: Combine Transformers ---
data_preprocessor = ColumnTransformer(transformers=[
    ('numerical', num_processor, num_cols),
    ('categorical', cat_processor, cat_cols)
])

# Step 6: Train-Test Split 
train_inputs, test_inputs, train_labels, test_labels = train_test_split(
    input_data, output_labels, test_size=0.33, random_state=42
)

# --- Step 7: Fit & Transform Data ---
train_inputs_processed = data_preprocessor.fit_transform(train_inputs)
test_inputs_processed = data_preprocessor.transform(test_inputs)

#_Step 8: Get Transformed Column Names ---
encoded_cols = data_preprocessor.named_transformers_['categorical']['encode'].get_feature_names_out(cat_cols)
final_columns = num_cols + list(encoded_cols)

# --Step 9: Save Results
pd.DataFrame(train_inputs_processed, columns=final_columns).to_csv("train_features_v2.csv", index=False)
pd.DataFrame(test_inputs_processed, columns=final_columns).to_csv("test_features_v2.csv", index=False)
pd.DataFrame({'label': train_labels}).to_csv("train_labels_v2.csv", index=False)
pd.DataFrame({'label': test_labels}).to_csv("test_labels_v2.csv", index=False)

print("\nPreprocessing completed and data saved successfully!")