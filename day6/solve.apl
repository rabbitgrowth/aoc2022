x←⊃⊃⎕NGET'input.txt'1
f←1-⍨⊣+⊣⍳⍨∘(≢¨)∪/
⎕← 4 f x
⎕←14 f x
⍝ original solution with ⌺:
⍝ f←{1-⍨⍺+⍺⍳⍨≢⍤∪⍤1⊢(⌊2÷⍨⍺-1)(-⍤⊣↓↓)⊢⌺⍺⊢⍵}
