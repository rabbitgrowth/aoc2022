⎕←4 14(1-⍨⊣+⊣⍳⍨∘(≢¨)∪/)¨⊃⎕NGET'input.txt'1
⍝ original solution with ⌺:
⍝ ⎕←4 14{1-⍨⍺+⍺⍳⍨≢⍤∪⍤1⊢(⌊2÷⍨⍺-1)(-⍤⊣↓↓)⊢⌺⍺⊢⍵}¨⊃⎕NGET'input.txt'1
