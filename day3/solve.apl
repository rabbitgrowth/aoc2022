n←(⎕A,⍨⎕C⎕A)∘⍳¨⊃⎕NGET'input.txt'1
⎕←+/{⊃⊃∩/↓⍵⍴⍨2,2÷⍨≢⍵}¨n
⎕←{+/{⊃⊃∩/⍵}¨↓⍵⍴⍨3,⍨3÷⍨≢⍵}n