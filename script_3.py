import numpy as np
from scipy.stats import norm

# Hypothetical data from multiple studies
study_results = [1.2, 1.5, 0.9, 1.3, 1.4]  # Effect sizes
study_variances = [0.1, 0.2, 0.15, 0.1, 0.2]

# Calculate weighted average effect size
weights = [1/var for var in study_variances]
weighted_avg_effect_size = np.average(study_results, weights=weights)
print("Weighted Average Effect Size:", weighted_avg_effect_size)

# Calculate combined variance
combined_variance = 1 / sum(weights)
print("Combined Variance:", combined_variance)

# Calculate confidence interval
z = norm.ppf(0.975)  # 95% confidence
ci_lower = weighted_avg_effect_size - z * np.sqrt(combined_variance)
ci_upper = weighted_avg_effect_size + z * np.sqrt(combined_variance)
print("95% Confidence Interval:", (ci_lower, ci_upper))
