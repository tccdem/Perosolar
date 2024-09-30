## Discovering Novel Lead-Free Mixed CationHybrid Halide Perovskites via Machine Learning

This repository contains code for calculating descriptors, training multiple machine learning models choosing the model with the minimum Mean Squared Error (MSE) to make predictions on novel perovskite materials.
The methodology employed leverages descriptors, such as ionic radii and electronegativity, as well as empirical factors like octahedral and tolerance factors, to construct a comprehensive feature set for each material. Using these features, thousands of machine learning models are trained and evaluated, with the best-performing model being selected based on its predictive accuracy.
Once a robust model is identified, it is utilized to predict the formation energy and band gap of unexplored perovskite configurations. The results are systematically analyzed through error plots, feature importance visualizations, and comprehensive performance metrics to validate the effectiveness of the predictive model.
This framework provides an efficient and scalable approach for the accelerated screening and discovery of promising lead-free perovskite materials, facilitating further exploration and validation through density functional theory (DFT) calculations.
![Perovskite_TOC](https://github.com/user-attachments/assets/5dc69ad8-92c4-4673-aef6-086e847fcb1a)

## Formation Energy Prediction
Prerequisites
The required packages can be found in the requirements.txt file. Make sure to install them using:
pip install -r requirements.txt
Code Files
1. Classic-Features_FE.py
Calculates classical descriptors for the elements involved, such as:

A_radius_dict: Radius of $A$-cations.
B_radius_dict: Radius of $B$-ions.
B_electro_dict: Electronegativity of $B$-ions.
X_radius_dict: Radius of $X$-anions.
2. Tol-Oct-features_FE.py
Calculates octahedral and tolerance factors for the perovskites, helping to narrow down the potential candidates.

3. pymatgen_descriptors.py
Utilizes pymatgen to generate additional structural and chemical descriptors for machine learning.

4. ML_saveCSV_FE_V2.py
Generates thousands of machine learning models with different parameters and calculates performance metrics to find the optimal model with the lowest MSE.

5. Find-min-mse_test_FE.py
Finds the model with the minimum MSE error and saves it for further use.

6. Pred-Load-FE.py
Loads the selected model to predict materials' formation energy.

7. Bar-plot-fea-impo_FE.py
Generates a plot to visualize the feature importance of the selected model, aiding in the interpretation of key descriptors.

8. MLErrorPlot_FE.py
Creates error plots comparing the predicted and actual values for both the training and test datasets, providing a visual representation of model performance.

##Bandgap Prediction
