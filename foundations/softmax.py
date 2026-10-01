import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        clean_z = z - np.max(z)

        z_i_arr = np.exp(clean_z)

        sum_z_j = np.sum(z_i_arr)

        p = z_i_arr/sum_z_j

        return np.round(p, 4)
