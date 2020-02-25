!conda install -c conda-forge swifter

import swifter
df['e'] = df.swifter.apply(lambda x : func(x['a'], x['b']),axis=1)
