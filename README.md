# Data-Mining-Project
STATS 415

Shengqian Jin (003); Hao Xu(003); Xinye Xu(002)

### Procedures:
1. Data exploration ACF Plots - Absolute Values (STATS 509)

2. How to deal with NA values (replace with historical value/ drop)

### New Data
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

Banking & Marketing: 
http://archive.ics.uci.edu/ml/datasets/Bank+Marketing

### Idea:

Propose data mining approaches to predict the success of telemarketing calls for selling bank long-term deposits.


### Writting Syllabus for STATS 415 Project: 
1. Preliminary

  (1) Data Exploration 

   (i) Visualization
   
   - Correlation (Graphical Correlation Matrix)
      
   - Boxplot: each X vs. Y (only most correlated X's)
       
   - Scatterplot: pairwise X vs. Y (ditto)
       
   (ii) Issues (try to find as many as possible features):
   
   - Which are most correlated?
       
   - Which exist classification trend?
       
   - Others
       
  (2) Split Data Set into Training and Test Data

   Issues need to claim: claim the features for time series data splittig.


2. Supervised Classification

Note: We are planning to use LDA, QDA, Logistic, and KNN. Therefore only use AIC, BIC, PCR, and PLS as dimension reduction methods, since: (i) forward/backward - need p-values (parametric), LDA, QDA, and KNN are non-parametric; (ii) rigde and lasso are not used in classification problems (and need beta's to be shrunk).

(1) Subset Selection Methods (AIC/BIC)

For each method of LDA, QDA, logit, and KNN, use AIC/BIC find the best one (with minimal AIC/BIC); reconstruct the final model then calculate the corresponding training and test errors.

(2) Dimension Reduction Methods (PCR/PLS)

   (i) Dimension Reduction
   
   PCR/PLS applied
       
   (ii) New X's
   
   Use Z's (projected from X's) then apply LDA, QDA, logit, and KNN; find corresponding errors.
       
(3) Best Model

Only compare training and test errors; claim clearly that cross-validation is not proper for time series data.

3. Clustering (Unsupervised Methods)

   (*TBD*)
   
4. Limitations and Conclusion

   (*TBD*)


### Reference

Relevant Papers:

S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014


Data Source:UCI Bank Marketing Data Set 

http://archive.ics.uci.edu/ml/datasets/Bank+Marketing
