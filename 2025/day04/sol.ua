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

FindRemovable ← ×⊸(≡(↘¯1↘1)↘¯1↘1 ⬚0⧈(≤4/+♭)3_3)

Part₁ ← /+/+FindRemovable
Part₂ ← -⊙(/+/+)⊸(/+/+⍥(-⊸FindRemovable)∞)

⊃Part₂ Part₁ Parse Input

┌─╴tests
  ˙⍤ =13 Part₁ Parse TestInput
  ˙⍤ =43 Part₂ Parse TestInput
└─╴
