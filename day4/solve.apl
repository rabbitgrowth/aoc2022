a b c d←↓⍉↑⍎¨'-'⎕R','⊃⎕NGET'input.txt'1
⎕←+/((a≥c)∧b≤d)∨(a≤c)∧b≥d
⎕←+/(b≥c)∧a≤d
