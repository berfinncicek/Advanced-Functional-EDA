# ADVANCED FUNCTIONAL EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

df = sns.load_dataset("titanic")

##check data

def check_df(dataframe, head=5):
    print("__Shape__")
    print(dataframe.shape)
    print("__Types__")
    print(dataframe.dtypes)
    print("__Head__")
    print(dataframe.head())
    print("__Tail__")
    print(dataframe.tail())
    print("__NaN__")
    print(dataframe.isnull().sum())
    print("__Quantiles__")
    print(dataframe.describe().T)
check_df(df)  



def grap_col_names(dataframe, cat_th =10, car_th = 20):
 
    
    ##categorical data

    cat_cols =[col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    
    num_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]] 
    
    cat_car = [col for col in df.columns if 
               df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]] 
    
    
    cat_cols = cat_cols + num_cat
    cat_cols = [col for col in cat_cols if col not in cat_car]
    
   ##numerical data

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols] 

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_car: {len(cat_car)}')
    print(f'num_cat: {len(num_cat)}')
    
    return cat_cols, num_cols, cat_car

cat_cols, num_cols, cat_car = grap_col_names(df)

    

def cat_summary(dataframe, col_name):
      print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                          "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
      
      print("---------------------------------------------------------")

    
cat_summary(df, "sex")    

for col in cat_cols:
   cat_summary(df,col) 
   
def num_summary(dataframe,numerical_col, plot = False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 1]
    print(dataframe[numerical_col].describe(quantiles).T)
    
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)
        
num_summary(df, "age", plot = True)   

for col in num_cols:
    num_summary(df,col,plot=True)
    
    
#categorical - graphical

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        
        
cat_cols, num_cols, cat_car = grap_col_names(df)    
       
    
def cat_Summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    
    print("---------------------------------------------------------")
    
    if plot:
        sns.countplot(x=dataframe[col_name],data = dataframe)
        plt.show(block = True)
    
for col in cat_cols:
   cat_Summary(df,col, plot = True)    
    
   
#target variable

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET MEAN": dataframe.groupby(categorical_col)[target].mean()}), end = "\n\n\n")
    
    
target_summary_with_cat(df, "survived", "pclass")    

for col in cat_cols:
    target_summary_with_cat(df, "survived",col)
    
    
def target_summary_with_num(dataframe, target,numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end = "\n\n\n")


for col in num_cols:
    target_summary_with_num(df, "survived",col)
    
    
    
#correlation analysis!!!

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
df = pd.read_csv("EDA_/datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

df_num = df[num_cols]


corr = df_num.corr()

sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()



def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
   
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype in [int, float]]
    df_num = dataframe[num_cols]
    
    corr = df_num.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    
    if plot:
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    
    return drop_list


drop_list = high_correlated_cols(df, plot=True)
df_filtered = df.drop(drop_list, axis=1)


drop_list_filtered = high_correlated_cols(df_filtered, plot=True)
df_filtered.drop(drop_list_filtered, axis=1)




    




