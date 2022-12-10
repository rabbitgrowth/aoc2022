⎕IO←0
noop←0 1
addx←,∘2
∆x cycles←↓⍉↑⍎¨⊃⎕NGET'input.txt'1
x←(cycles,0)/+\1,∆x
⎕←+/i×x[1-⍨i←20+40×⍳6]
⎕←' ⎕'[6 40⍴1≥|x-40|⍳240]
