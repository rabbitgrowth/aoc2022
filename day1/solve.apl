x←{⍵[⍒⍵]}(+/⍎¨)¨((×≢¨)⊆⊢)⊃⎕NGET'input.txt'1
⎕←⊃x
⎕←+/3↑x
