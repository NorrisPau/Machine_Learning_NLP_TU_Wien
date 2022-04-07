ML_NLP_OKCupid
==============================

Using NLP to analyze OkCupid profile texts for my class 

--------

## Organization


           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data 
    ├── raw data                 <- The original, immutable data dump.
    ├── processed                <- The final, canonical data sets for modeling.
├── scripts
    ├── data_processing.py
├── notebooks
    ├── dat_exploration

## Dataset
The Dataset okcupid_profiles.csv comes from Kaggle and can be directly downloaded [here](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles). 

**Demographic Variables are:**  
* age
* status
* sex
* orientation
* body type
* diet
* drinks
* drugs
* education
* ethnicity
* height
* income
* job
* last_online
* location
* offspring
* pets
* religion
* sign
* smokes
* speaks


**Essay Questions are:**
* essay0: About Me / Self summary
* essay1: Current Goals / Aspirations
* essay2: My Golden Rule / My traits
* essay3: I could probably beat you at / Talent
* essay4: The last show I binged / Hobbies
* essay5: A perfect day / Moments
* essay6: I value / Needs
* essay7: The most private thing I'm willing to admit / Secrets
* essay8: What I'm actually looking for / Dating
