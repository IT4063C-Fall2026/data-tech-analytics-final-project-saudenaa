#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
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

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# ###1.World Bank API — health spending per capita (SH.XPD.CHEX.PC.CD) [API]
# ###2.World Bank API — life expectancy at birth (SP.DYN.LE00.IN) [API]
# ###3.IHME Global Burden of Disease — neurological disease burden by country (CSV) [File]

# In[1]:


# Start your code here


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

