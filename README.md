# Data-Mining-Project
STATS 415

Shengqian Jin (003); Hao Xu(003); Xinye Xu(002)

### Procedures:
1. Data exploration ACF Plots - Absolute Values (STATS 509)

2. How to deal with NA values (replace with historical value/ drop)

### New Data

CBOE Crude Oil ETF Volatility Index: OVXCLS

Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma (DCOILWTICO)	

ICE BofAML US Corp AAA Total Return Index Value (BAMLCC0A1AAATRIV)

Dow Jones Industrial Average (DJIA)

NASDAQ Composite Index (NASDAQCOM)

ICE BofAML BB Emerging Markets Corporate Plus Sub-Index Total Return Index Value (BAMLEM3BRRBBCRPITRIV)

ICE BofAML US High Yield Master II Total Return Index Value (BAMLHYH0A0HYM2TRIV)	

Wilshire 5000 Total Market Full Cap Index (WILL5000INDFC)	
 
CBOE Gold ETF Volatility Index (GVZCLS)

### Agenda: 

3/23 or Spring Break: 

Shengqian Jin: time series cross-validation, dimensional reduction (PCA), Model Selection, 

Hao Xu: summary statistics, K nearest neighbors; Linear and Quadratic Discriminant Analysis; Logistic regression, similar to HW framework

Xinye Xu: summary visualization, Trees (Bayesian regression addictive tree), (K-means),  LSTM, 



### Idea:

We want to test whether past related asserets price can predict the movement direction of bond market (AAA bond) and stock market (S&P500) in US of future dates. These features include Fed interest rate, VIX index, Exchange rate of US with China and EU, Emerging bond index. 
Both supervised and Unsupervised techniques, such as KNN, Linear and Quadratic Discriminant Analysis, Bayesian regression addictive tree. Also, the more advanced models, such as Long Short Term Memory networks (LSTM) might be used as the benchmarket to compare the performance.  Lastly, we will apply Model Selection methodologeis to compare the performance of differed model and discuss futuere improvement. 


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



Data Source: Federal Reserve Economic Data

questions: 
https://www.iaqf.org/dev/files/IAQF%20Competition%20Problem%202017.pdf

papers: 

https://www.iaqf.org/news/news_detail/49


Report Edit:

https://www.overleaf.com/1479489434yjxvtpxhnkmf

https://zhuanlan.zhihu.com/p/21659522
