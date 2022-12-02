#!/usr/local/bin/dyalogscript
⎕IO←0
m←3|'ABCXYZ'⍳1 0 1/↑⊃⎕NGET'input.txt'1
⎕←(+/(1+⊢/)+3×3|1+-⍨/)m
⎕←(+/(3×⊢/)+1+3|1-⍨+/)m
