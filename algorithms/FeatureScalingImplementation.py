import numpy as np

def feature_scaling(data: np.ndarray):
	
	standardized_data = (data - np.mean(data, 0)) / np.std(data, 0)
	
	rangeX = np.max(data, 0) - np.min(data, 0)

	normalized_data = (data - np.min(data, 0)) / rangeX
	
	return standardized_data, normalized_data
