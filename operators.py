from qiskit.quantum_info import Pauli, Operator, DensityMatrix, Statevector
import numpy as np

IPSTATE = Statevector([1/np.sqrt(2), 1j*1/np.sqrt(2)])
IMSTATE = Statevector([1/np.sqrt(2), -1j*1/np.sqrt(2)])


def real_state(state:DensityMatrix):
    return 1/2*(state.tensor(IPSTATE)+state.conjugate().tensor(IMSTATE))


if __name__=='__main__':
    state = DensityMatrix([[1, 0],[0, 1]])
    print(real_state(state))