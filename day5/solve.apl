par1 par2←((×≢¨)⊆⊢)⊃⎕NGET'input.txt'1
temp←((~∘' '¨⍤↓⍤⍉⊢⊢⍤/⍨0 1 0 0⍴⍨≢⍤⍉)¯1↓↑)par1
steps←(⍎¨'\d+'⎕S'&')¨par2
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
