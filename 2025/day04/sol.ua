TestInput ← $ ..@@.@@@@.
            $ @@@.@.@.@@
            $ @@@@@.@.@@
            $ @.@@@@..@.
            $ @@.@@@@.@@
            $ .@@@@@@@.@
            $ .@.@.@.@@@
            $ @.@@@.@@@@
            $ .@@@@@@@@.
            $ @.@.@@@.@.
Input     ← &fras "input"

Parse ← ⊜(=@@)⊸≠@\n

FindRemovable ← ×⊸(<4/+⬚0↻⊂C₂A₂)

Part₁ ← /+/+FindRemovable
Part₂ ← -⊙(/+/+)⊸(/+/+⍥(-⊸FindRemovable)∞)

⊃Part₂ Part₁ Parse Input

┌─╴tests
  ˙⍤ =13 Part₁ Parse TestInput
  ˙⍤ =43 Part₂ Parse TestInput
└─╴
