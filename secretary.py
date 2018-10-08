#Solving the probabilities for the Secretary problem
import math
import matplotlib.pyplot as plt

cand_list = range(3,16)
print([i for i in cand_list])

optimal_sample_size_k = [int(round(i/2.71,0)) for i in cand_list]
print([i for i in optimal_sample_size_k])

ratio_k_n = [round(optimal_sample_size_k[i]/cand_list[i],4) for i in range(len(optimal_sample_size_k))]
print(ratio_k_n)

approx_prob_success_p = [round((i*math.log(i)*-1),4) for i in ratio_k_n]
print(approx_prob_success_p)

fig, ax = plt.subplots()

ax.plot(approx_prob_success_p)
