ising_dir = '' #Insert the name of the directory containing the Python dictionaries to be submitted to D-Wave.
savedir = '' #Insert the name of the directory where the results from D-Wave will be saved.

ising_name = '' #Insert the file name of the Python dictionary to be submitted to D-Wave.
fname = '' #Insert the file name of the results file where the D-Wave output will be saved.

ising = eval(open(ising_dir+ising_name, "r").read()) #Read the input Python dictionary in Ising form.
h = {} #Initialize the longitudinal field h dictionary.
for i in range(num_of_nodes[ind-1]): #Set h to 0 for all qubits.
    h[(i)] = 0.

bqm = dimod.BQM.from_ising(h,ising) #Translate the input Ising Python dictionary and h to the BQM form.

result = LeapHybridSampler(profile='').sample(bqm) #Insert your profile from the D-Wave Ocean configuration file - default is "default". LeapHybridSampler() samples from the D-Wave Hybrid solver.

res_df = result.to_pandas_dataframe() #Convert the output from D-Wave to a Pandas dataframe.

with open(savedir+fname+'_info.txt', "w") as f: #Save the output from D-Wave into the specified file.
    f.write(str(result.info))
res_df.to_csv(savedir+fname+'_results.csv')