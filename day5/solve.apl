p1 p2←((×≢¨)⊆⊢)⊃⎕NGET'input.txt'1
temp←((~∘' '¨⍤↓⍤⍉⊢⊢⍤/⍨0 1 0 0⍴⍨≢⍤⍉)¯1↓↑)p1
steps←(⍎¨'\d+'⎕S'&')¨p2
move←{
    x y z←⍵
    items←⍺⍺x↑y⊃stacks
    (y⊃stacks)↓⍨←x
    (z⊃stacks),⍨←items
}
stacks←temp ⋄ ⌽move¨steps
⎕←⊃¨stacks
stacks←temp ⋄ ⊢move¨steps
⎕←⊃¨stacks
