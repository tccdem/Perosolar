## Formation Energy Prediction

This repository contains code for calculating descriptors, training multiple machine learning models choosing the model with the minimum Mean Squared Error (MSE) to make predictions on novel perovskite materials.
The methodology employed leverages descriptors, such as ionic radii and electronegativity, as well as empirical factors like octahedral and tolerance factors, to construct a comprehensive feature set for each material. Using these features, thousands of machine learning models are trained and evaluated, with the best-performing model being selected based on its predictive accuracy.
Once a robust model is identified, it is utilized to predict the formation energy and band gap of unexplored perovskite configurations. The results are systematically analyzed through error plots, feature importance visualizations, and comprehensive performance metrics to validate the effectiveness of the predictive model.
This framework provides an efficient and scalable approach for the accelerated screening and discovery of promising lead-free perovskite materials, facilitating further exploration and validation through density functional theory (DFT) calculations.
![Perovskite_TOC](https://github.com/user-attachments/assets/5dc69ad8-92c4-4673-aef6-086e847fcb1a)
