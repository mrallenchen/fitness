
### Data Collection

Downloaded data from the National Health and Nutrition Examination Survey (continuously conducted by CDC's National Center for Health Statistics) \
- https://www.cdc.gov/nchs/nhanes/index.htm \
- Survey cycles collected for NHANES data : 2011-2012, 2013-2014, 2015-2016, 2017-2018\
- Additional detail on Data Collection methodology shown in [Data Collection and EDA Notebook](../Data_Collection_EDA.ipynb)


Also collected information on Weight Status and Fitness Status, from other sources


### I. Tables in the SQL Database

| Table | Title | Primary Data| Source |
| --- | ---- | ---- | ----- |
| **BMI_CAT** | Weight Status | Status by gender and BMI | [CDC](https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html)
| **BMX** | [Body Measures (BMX_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm) | BMI, length, circumference info | CDC - NHANES |
| **DBQ** | [Diet Behavior and Nutrition (DBQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DBQ_J.htm)|  Milk preferences, school meals, meal prep | CDC - NHANES |
| **DEMO** | [Demographics (DEMO_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm)  | Survey cycle, age, gender  | CDC - NHANES |
| **DR** | [Dietary Interview (Dr1TOT_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR1TOT_J.htm) | Type of diet (low carb, high protein, etc) | CDC - NHANES |
| **DXX** | [DEXA Scan: Dual-Energy X-ray Absorptiometry - Whole Body (DXX_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DXX_J.htm) | Body fat % (including by body part) | CDC - NHANES |
| **FAT** | Fitness Level| Fitness based on body fat% | [American Counsel on Exercise](https://www.acefitness.org/education-and-resources/lifestyle/tools-calculators/percent-body-fat-calculator/)
| **PAQ** | [Physical Activity (PAQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/PAQ_J.htm) | Exercise frequency | CDC - NHANES |
| **WHQ**| [Weight History (WHQ_J)](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/WHQ_J.htm) | Self image, weight history, weight loss strategies e.g. skipping meals, eat less, diet, weight loss program, laxatives |  CDC - NHANES |



