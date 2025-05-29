# DATA-PIPELINE-DEVELOPMENT

COMPANY: CODETECH IT SOLUTION

NAME: RASHMI KUMARI 

INTERN ID:CT04DN978

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

TASK DESCRIPTION :
               Introduction
In the early stages of any data science project, the most critical activity is preparing the data so it is clean, consistent, and suitable for analysis or modeling. This process, called data preprocessing, is the foundation upon which meaningful insights and predictive models are built. My primary task was to construct a modular, automated data pipeline using Python, Pandas, and Scikit-learn to handle these preprocessing operations in a manner that is not only systematic and error-resistant but also repeatable and scalable for real-world workflows.

Step 1: Understanding the Dataset
The first step was to understand and load the raw data. For this task, a CSV file named sample_data.csv was used, containing numeric features like 'age' and 'salary', categorical features such as 'department' and 'city', and a binary 'target' column. Typically, real-world datasets may have formatting issues, missing values, or mixed data types; I kept these challenges in mind from the start.

To load this dataset, I used the Pandas library, which offers a straightforward function read_csv. Anticipating possible errors, such as missing files or incorrect paths, I wrapped this call in a try-except block to ensure robust code execution—a recommended practice in both industry and academia.

Step 2: Separating Features and the Target
Once the data was loaded successfully, I split the DataFrame into two distinct parts:

Input features (X): All columns except the target.
Output labels (y): The 'target' column.
This separation is crucial. By isolating features from the outcome, it prevents data leakage—where information from the target variable could inadvertently influence the feature transformations. Such separation honors the requirement that preprocessing should never use information from the target when fitting on training data.

Step 3: Identifying Numeric and Categorical Columns
The next step involved specifying which columns are numeric and which are categorical.

Numeric columns included 'age' and 'salary'.
Categorical columns consisted of 'department' and 'city'.
While this process could be automated, explicitly listing these columns ensures clarity and avoids mistakes (such as misclassification due to ambiguous data types), which is especially important on internship or beginner projects.

Step 4: Designing Preprocessing Pipelines for Each Data Type
With columns categorized, I created dedicated pipelines for preprocessing:

Numeric Pipeline: This handled missing values using SimpleImputer(strategy='mean'), replacing gaps with the mean, then scaled values using StandardScaler() so all numeric features have similar importance and are on comparable scales.
Categorical Pipeline: Here, missing values were substituted with the most frequent (mode) value using SimpleImputer(strategy='most_frequent'), before transforming categories into binary vectors with OneHotEncoder(handle_unknown='ignore', sparse_output=False). This ensures that machine learning models can interpret categorical data as numbers.
Step 5: Combining Pipelines with ColumnTransformer
To make preprocessing modular and clean, I combined the numeric and categorical pipelines using Scikit-learn’s ColumnTransformer. This smart tool applies different transformations to specified columns in parallel and guarantees the correct order of output features. Such structure preserves code readability, reproducibility, and error handling, all essential for team projects and professional environments.

Step 6: Splitting the Data for Training and Testing
Before fitting the pipeline, I split the data into training and testing sets using train_test_split. This simulates real-world practice where models must be trained on historical data and evaluated on unseen data. A 67/33 split was chosen, as is common with smaller datasets. Ensuring the pipeline is fitted only on training data avoids the risk of information leakage, further upholding best practices.

Step 7: Fitting and Transforming the Data
Now, I fitted the transformer only to the training data. This step “learns” all necessary parameters (like column means, modes, and scaling factors) using just the training set. Both fit_transform (on training data) and transform (on test data) are used to ensure the pipeline remains unbiased. Maintaining this separation is critical for fair and trustworthy model evaluations.

Step 8: Handling Transformed Features and Saving Results
Categorical encoding transforms columns into new binary features. Therefore, I extracted the new column names using the encoder’s get_feature_names_out method and combined these with the numeric column names to form a comprehensive list. Finally, I saved both the transformed training and testing features, as well as their labels, into separate CSVs using Pandas’ to_csv method. This “load” step ensures downstream analysis or modeling can proceed from clean, ready-to-use datasets.

Conclusion
This task closely followed what is typically described in Data Science internship guides and the references in 'DATA SCIENCE.pdf': automate the data cleaning, transformation, and partitioning processes using industry-standard tools and best practices. Every decision—from using explicit column lists to error handling—reflects a mindset of professionalism and reliability. This pipeline is not just a one-off script but a template for robust, future data science work.

In summary:
The preprocessing and pipeline construction task required understanding raw data, carefully splitting and categorizing it, building modular transformation pipelines, combining them cleanly, and saving the final prepped data for analysis—all while making sure code was readable, maintainable, and industrially sound. These practices form the core of any practical Data Science ETL pipeline and serve as foundational skills for any aspiring data scientist.
