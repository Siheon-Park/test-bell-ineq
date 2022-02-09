from sre_parse import State
from qiskit.quantum_info import Pauli, Operator, DensityMatrix, Statevector
from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
import numpy as np

IPSTATE = Statevector([1/np.sqrt(2), 1j*1/np.sqrt(2)])
IMSTATE = Statevector([1/np.sqrt(2), -1j*1/np.sqrt(2)])
_qc_ = QuantumCircuit(2, name='Bell Op')
_qc_.h(0)
_qc_.cnot(0, 1)
BELL_OP = Operator(_qc_)


def real_state(state:DensityMatrix):
    return 1/2*(state.tensor(IPSTATE)+state.conjugate().tensor(IMSTATE))

def real_meas_op(meas:Operator):
    return meas.tensor(IPSTATE)+meas.conjugate().tensor(IMSTATE)

class CHSH3ComplexQuantumGame:
    def __init__(self):
        super().__init__()
        qa = QuantumRegister(1, name='alice')
        qb = QuantumRegister(2, name='bob')
        qc = QuantumRegister(1, name='chalie')
        cr = ClassicalRegister(4)
        qc = QuantumCircuit(qa, qb, qc, cr)
        qc.compose(BELL_OP.to_instruction(), qubits=(0, 1), inplace=True)
        qc.compose(BELL_OP.to_instruction(), qubits=(3, 4), inplace=True)
        qc.compose(BELL_OP.to_instruction().adjoint(), qubits=(1, 2), inplace=True)
        qc.compose


    def A(x):
        """
            return Alice's measurement op
        """
        return Pauli(['Z', 'X', 'Y'][x])

    def C(z):
        """
            return Chalie's measurement op
        """

if __name__=='__main__':
    state = BELL_OP.tensor(BELL_OP)
    qc = QuantumCircuit(4, 4)
    qc.compose(state.to_instruction(), inplace=True)
    qc.compose(BELL_OP.adjoint().to_instruction(), qubits=(1, 2), inplace=True)
    print(qc)