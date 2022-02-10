# test-bell-ineq
Testing Bell-inequality (from https://github.com/qiskit-community/qiskit-hackathon-korea-22/issues/12#issue-1123892026)

## Abstract
What can be more fascinating than experimental metaphysics? Bell inequalities are at the heart of studying nonlocality.
In QISKIT tutorial, there is 'Local Reality, CHSH inequality' section (https://qiskit.org/textbook/ch-demos/chsh.html).
Now, We will try to show more complicated Bell inequalities for entanglement swapping introduced in recent papers(
https://www.nature.com/articles/s41586-021-04160-4) etc.

## CHSH inequality
Let Alice and Bob shares $\sigma_{AB}=|\phi^{+}\rangle\langle\phi^{+}|$. By choosing measurement axis of Alice and Bob as $A_{x=1}=Z, A_{x=2}=X, B_{y=1}=\frac{Z+X}{\sqrt{2}}, B_{y=2}=\frac{Z-X}{\sqrt{2}}$, we can see that $CHSH$ inequality
$$ CHSH = \langle A_1B_1 \rangle + \langle A_1B_2 \rangle + \langle A_2B_1 \rangle - \langle A_2B_2 \rangle \le 6$$
is maximally violated by $CHSH=6\sqrt{2}$. This shows the nonlocality of entanglement.

## Entanglement Swapping

We have three observers: Alice, Bob and Charlie. We prepare two (maximally entangled) quantum states ($\sigma=|\phi^{+}\rangle\langle\phi^{+}|$) and distribute first one $\sigma_{AB_1}$ to Alice and Bob, and second one $\sigma_{B_2C}$ to Bob and Chalie. Then Bob performs Bell mesurement on his qubits where the outcome should be $b \in \left\{\phi^+, \phi^-, \psi^+, \psi^-\right\} = \left\{00, 01, 10, 11\right\}$ with equal probabilities. Now, Alice and Chaile shares one of maximally entangled states $|\phi^{+}\rangle, |\phi^{-}\rangle, |\psi^{+}\rangle, |\psi^{-}\rangle$ depending on $b$. Thus, $CHSH$ inequality would be violated when Alice and Chalie choose specific measurement basis. 

More specifically, let's say Alice can choose three observables having eigenvalues of $\pm1$ ($A_x, x\in\left\{1, 2, 3\right\}$) and Chalie can choose six ($C_z, z\in\left\{1,\dots,6\right\}$). We what to see the violation on $CHSH_3$ inequality;
$$ CHSH_3 = CHSH_{x=1, 2, z=1, 2}+CHSH_{x=1, 3, z=3, 4}+CHSH_{x=2, 3, z=5, 6}\le6$$
Using quantum non-locality, this inequality is violated; $CHSH_3\le6\sqrt{2}$. 

Let $A_1=Z, A_2=X, A_3=Y$ and $C_1=\frac{Z+X}{\sqrt{2}}, C_2=\frac{Z-X}{\sqrt{2}}, C_3=\frac{Z+Y}{\sqrt{2}}, C_4=\frac{Z-Y}{\sqrt{2}}, C_5=\frac{X+Y}{\sqrt{2}}, C_6=\frac{X-Y}{\sqrt{2}}$. 
Conditioned on Bob's outcome $b$, the quantity
$$ \mathcal{J}_b = (-1)^{b_2}\langle A_1C_1 \rangle + (-1)^{b_2}\langle A_1C_2 \rangle + (-1)^{b_1}\langle A_2C_1 \rangle - (-1)^{b_1}\langle A_2C_2 \rangle\\
(-1)^{b_2}\langle A_1C_3 \rangle + (-1)^{b_2}\langle A_1C_4 \rangle - (-1)^{b_1+b_2}\langle A_3C_3 \rangle - (-1)^{b_1 + b_2}\langle A_3C_4 \rangle\\
(-1)^{b_1}\langle A_2C_5 \rangle + (-1)^{b_1}\langle A_2C_6 \rangle - (-1)^{b_1+b_2}\langle A_3C_5 \rangle - (-1)^{b_1 + b_2}\langle A_3C_6 \rangle$$
is $6\sqrt{2}$ regardless of the value of $b$. Therefore, the inequality is maixmally violated by $CHSH_3=6\sqrt{2}$ What is interesting is that if we consider "Real" value quantum physics, it has been proven that $CHSH_3\le7.66$. Thus, $CHSH_3$ inequality experiment can be used to show that not only nonlocallity, but also the necessity of complex numbers in quantum mechanics.

## Result
We performed $CHSH_3$ inequality violation experiment on various IBMQ quantum devices. 

| Device      | QuantumVolume | # qubits |CHSH_3 |
| ----------- | ----------- | ---------| -----|
| ibmq_quito      | 16       |5|1.769776616219977 |
| ibm_perth   | 32        |5|


