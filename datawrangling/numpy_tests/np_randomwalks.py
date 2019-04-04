import numpy as np

nwalks = 5000
nsteps = 1000

draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks
walks.max()
walks.min()

hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum()