from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

modelo=BayesianNetwork([("S", "A"), ("R", "A"),("A", "J"),("A", "M")])
cpd_s=TabularCPD( variable ="S", variable_card =2, values =[[0.02] ,
[0.98] , ])
cpd_r=TabularCPD( variable ="R", variable_card =2, values =[[0.01] ,
[0.99] , ])
cpd_a=TabularCPD( variable ="A", variable_card =2, values =[[0.95,0.94,0.29,0.001],[0.05,0.06,0.71,0.999]],evidence=["S","R"],
evidence_card=[2,2])
cpd_j=TabularCPD( variable ="J", variable_card =2, values =[[0.9,0.01],[0.1,0.99]],evidence=["A"],
evidence_card=[2])
cpd_m=TabularCPD( variable ="M", variable_card =2, values =[[0.7,0.01],[0.3,0.99]],evidence=["A"],
evidence_card=[2])
modelo.add_cpds(cpd_s,cpd_r,cpd_a,cpd_j,cpd_m)


from pgmpy . inference import VariableElimination
infer = VariableElimination ( modelo )

posterior_p = infer . query (["R"], evidence ={"J": 1,"M":1})
print ( posterior_p)
