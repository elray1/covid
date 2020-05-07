import numpy as np
from pathlib import Path

root='results'
start='2020-03-15'
configs="SEIRD_incident"
#forecast_dates="2020-04-04 2020-04-11  2020-04-18 2020-04-25"   # validation
forecast_dates="2020-05-03" # this week's submission

states="AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY"
#states="AL AK"

for config in configs.split(' '):
    for forecast_date in forecast_dates.split(' '):
        samples_prefix = Path(root) / config / forecast_date / 'samples'
        medians_prefix = Path(root) / config / forecast_date / 'medians'
        medians_prefix.mkdir(parents=True, exist_ok=True)
        
        for place in states.split(' '):
            filename = samples_prefix / (place + '.npz')
            mcmc_output = np.load(filename, allow_pickle=True)
            mcmc_samples = mcmc_output['mcmc_samples'].item()
            
            post_medians = {key: np.median(mcmc_samples[key], axis = 0) \
                for key in mcmc_samples.keys()}
            
            filename = medians_prefix / (place + '.npz')
            np.savez(filename, post_medians=post_medians)
