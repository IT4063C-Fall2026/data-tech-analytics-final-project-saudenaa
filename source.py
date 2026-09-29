#!/usr/bin/env python
# coding: utf-8

# # Healthcare Spending and Neurological Disease
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->

# Neurological conditions like stroke, epilepsy, and dementia are a rising share of disease worldwide, but the resources to treat them aren't spread evenly across countries. This project examines whether higher healthcare spending relates to better health outcomes and lower neurological disease burden. It matters because it shows where investment could help most.

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# Does higher health spending relate to longer life expectancy and lower neurological disease burden across countries?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# I expect countries with higher health spending tend to have longer life expectancy and lower neurological disease burden, likely with diminishing returns. An answer looks like a scatter plot of spending vs. life expectancy with an upward trend line.

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# 1.World Bank API — health spending per capita (SH.XPD.CHEX.PC.CD) [API]<br>
# 2.World Bank API — life expectancy at birth (SP.DYN.LE00.IN) [API] <br>
# 3.IHME Global Burden of Disease — neurological disease burden by country (CSV) [File] <br>

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# I merge three datasets — health spending and life expectancy (World Bank API) and neurological disease burden (IHME CSV) — on country and year into one table. Then I use correlation and visualizations (scatter plots, heatmap) to see whether higher health spending relates to longer life expectancy and lower disease burden.

# In[7]:


# Start your code here
import requests
import pandas as pd

#-----Source-1(API) : World Bank health spending per capita ---
url1 = "https://api.worldbank.org/v2/country/all/indicator/SH.XPD.CHEX.PC.CD?format=json&per_page=20000"
d1 = requests.get(url1).json()[1]

spending = pd.DataFrame([{"country": x["country"]["value"],
                         "year"   : int(x["date"]),
                         "health_spending" : x["value"]}
                          for x in d1 if x["value"] is not None])

spending = spending[spending["year"] == 2023]

#-----Source-2(API) : World Bank Life Expectancy -----
url2 = "https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN?format=json&per_page=20000"
d2 = requests.get(url2).json()[1]

life = pd.DataFrame([{"country" : x["country"]["value"],
                      "year"    : int(x["date"]),
                      "life_expectancy": x["value"]}
                      for x in d2 if x["value"] is not None])


life = life[life["year"] == 2023]

#------Source-3(File):  IHME neurological diseases burden ---
neuro = pd.read_csv("IHME-GBD_2023_DATA.csv")
neuro = neuro[(neuro["cause_name"]  == "Neurological disorders") &
              (neuro["metric_name"] == "Rate") &
              (neuro["measure_name"] == "DALYs (Disability-Adjusted Life Years)")
             ]

neuro = neuro.rename(columns={"location_name": "country",
                              "val"          : "neuro_burden"          
                              })

neuro = neuro[["country", "year", "neuro_burden"]]

# ------Merge all three on country  + year --
df = spending.merge(life, on = ["country", "year"]).merge(neuro, on =["country", "year"])

print("Merged shape:", df.shape, "| Countries:", df["country"].nunique())
print(df.head())



# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# I import the two World Bank indicators via API and the IHME data from CSV, then merge them on country and year into one table for analysis.<br>
# 
# https://data360.worldbank.org/en/api <br>
# https://vizhub.healthdata.org/gbd-results/

# In[8]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

