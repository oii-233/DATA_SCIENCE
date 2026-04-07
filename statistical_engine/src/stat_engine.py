import math
from collections import Counter

class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("Dataset is empty after cleaning.")

    def _clean_data(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")

        cleaned = []
        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(item)
            else:
                try:
                    cleaned.append(float(item))
                except:
                    raise TypeError(f"Invalid data type: {item}")

        return cleaned

    # ---------------------------
    # Central Tendency
    # ---------------------------
    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = Counter(self.data)
        max_freq = max(freq.values())

        if max_freq == 1:
            return "No mode (all values unique)"

        modes = [k for k, v in freq.items() if v == max_freq]
        return modes

    # ---------------------------
    # Dispersion
    # ---------------------------
    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        n = len(self.data)

        squared_diff = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            if n < 2:
                raise ValueError("Sample variance requires at least 2 data points.")
            return sum(squared_diff) / (n - 1)
        else:
            return sum(squared_diff) / n

    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)

    # ---------------------------
    # Outliers
    # ---------------------------
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        return [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]