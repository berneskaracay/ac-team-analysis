# # %matplotlib inline

""
# # !pip install ipywidgets
# # !pip install -U -q ipywidgets
# # !pip install plotly
# # !pip install cufflinks

""
# # !jupyter nbextension enable --py widgetsnbextension

""
# # !pip install plotly --upgrade

""
# # !pip install chart_studio

""
print('Preparing ata For Analysis...')
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.lines import Line2D

import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import workdays

import matplotlib.pyplot as plt
# %matplotlib inline
#import seaborn as sns


import os
import sys
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from termcolor import colored
import time



import seaborn as sns
plt.style.use('ggplot')
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999
pd.options.display.max_colwidth = 999

from IPython.display import HTML as html_print

def cstr(s, color='black'):
    return "<text style=color:{}>{}</text>".format(color, s)





""
# Standard Data Science Helpers
import numpy as np
import pandas as pd
import scipy

import chart_studio.plotly as py
#import chart_studio.graph_objs as go
#from chart_studio.offline import iplot, init_notebook_mode
#init_notebook_mode(connected=True)

import cufflinks as cf
cf.go_offline(connected=True)
cf.set_config_file(colorscale='plotly', world_readable=True)

# Extra options
pd.options.display.max_rows = 30
pd.options.display.max_columns = 25

# Show all code cells outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

""
from IPython.display import Image, display, HTML

""
df=pd.read_csv("data//JIRA.csv")
df.shape

""


"""
### keep only completed tasks.
"""

df["completed"]=pd.to_datetime(df['Resolved'])
df["started"]=pd.to_datetime(df['Created'])

""
df = df.dropna(subset=["completed"]) 
df.shape

""
df["started"]=pd.to_datetime(df['Created'])

""
df = df.dropna(subset=["started"]) 
df.shape

###############################################################################
# ### created to updated

df["Updated_date"]=pd.to_datetime(df['Updated'])


###############################################################################
# ### last viewed

df["Updated_date"]=pd.to_datetime(df['Updated'])

""
df["time_to_updated"]=(df["Updated_date"]-df["started"]).astype('timedelta64[h]')

###############################################################################
# ### due date

df["due_date"]=pd.to_datetime(df['Due date'])

""
df["time_due_date"]=(df["due_date"]-df["started"]).astype('timedelta64[h]')

###############################################################################
# ## Efficiency   - excluding ongoing/recurring tickets

df["time_to_complete"]=(df["completed"]-df["started"]).astype('timedelta64[h]')

""
df.insert(loc=0, column = 'total_days', value = 0)

""
for index, row in df.iterrows():
    df.at[index,'total_days'] = np.busday_count(row['started'].date(),row['completed'].date()) #set UBR1_RaceEthnicity field to value returned from UBRRaceEthnicity() 

###############################################################################
# ### recurring

df["RECURRING"]=0

""
df.loc[df['Summary'].str.contains("RECURRING",case=False),["RECURRING"]]=1

###############################################################################
# ### comment 

# df["RECURRING"]=0
# df.loc[df['Summary'].str.contains("RECURRING",case=False),["RECURRING"]]=1


""

comment_df=df.loc[:,df.columns.str.contains('Comment')]

""
comment_df.head(1)

""
comment_df['full_count'] = comment_df.apply(lambda x: x.count(), axis=1)

###############################################################################
# ### Ad Hoc

df["AdHoc"]=0

""
df.loc[df['Summary'].str.contains("Ad Hoc",case=False),["AdHoc"]]=1

###############################################################################
# ### CDR

df["CDR"]=0

""
df.loc[df['Summary'].str.contains("CDR ",case=False),["CDR"]]=1

###############################################################################
# ### RDR

df["RDR"]=0

""
df.loc[df['Summary'].str.contains("RDR",case=False),["RDR"]]=1

###############################################################################
# ### Data pull

df["Data pull"]=0

""
df.loc[df['Summary'].str.contains("Data pull",case=False),["Data pull"]]=1

###############################################################################
# ## Busy season - use all tickets since the inception of the board

###############################################################################
# One version with recurring/ongoing tickets included

df["started"]=pd.to_datetime(df['Resolved'])
df["started1"]=df.started.map(lambda x: x.strftime('%Y-%m-%d'))
df['started1'] = pd.to_datetime(df['started1'], errors='coerce')

""
df["completed"]=pd.to_datetime(df['completed'])
df["completed1"]=df.completed.map(lambda x: x.strftime('%Y-%m-%d'))
df['completed1'] = pd.to_datetime(df['completed1'], errors='coerce')

""
df_nore=df[df.RECURRING != 1]

""
df_nore["started"]=pd.to_datetime(df_nore['Created'])
df_nore["started1"]=df_nore.started.map(lambda x: x.strftime('%Y-%m-%d'))
df_nore['started1'] = pd.to_datetime(df_nore['started1'], errors='coerce')

""


""
print('Done.')

""


""


""


""


""

