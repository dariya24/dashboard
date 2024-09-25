import numpy as np
import pandas as pd
import scipy.stats.distributions as dist
from statsmodels.stats.proportion import proportions_ztest

def get_pvalue_propotion(df, var1, var2):
    groups = df[var2].unique()
    groupA = groups[0]
    groupB = groups[1]
    contingency_table = pd.crosstab(df[var1], df[var2]).reset_index()  # Contingency Table
    A00 = int(contingency_table[contingency_table[var1] == 0][groupA])
    A01 = int(contingency_table[contingency_table[var1] == 0][groupB])
    A10 = int(contingency_table[contingency_table[var1] == 1][groupA])
    A11 = int(contingency_table[contingency_table[var1] == 1][groupB])

    print("{}: {}, {}:{}".format(groupA, A00 / (A00 + A10), groupB, A01 / (A01 + A11)))

    count = np.array([A00, A01])
    nobs = np.array([A00 + A10, A01 + A11])
    stat, pval = proportions_ztest(count, nobs)
    if pval < 0.005:
        significant = 1
        text = "Statistically significant, pValue <0.005"
        color = "green"
    else:
        significant = 0
        text = "NOT statistically significant, pValue {0:.3f}".format(pval)
        color = "red"

    return text, color