⎕IO←0
x←3|'ABCXYZ'⍳1 0 1/↑⊃⎕NGET'input.txt'1
⎕←(+/(1+⊢/)+3×3|1+-⍨/)x
⎕←(+/(3×⊢/)+1+3|1-⍨+/)x
