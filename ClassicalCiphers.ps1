#still needs testing

$ORDVAL_A = 65
$ORDVAL_a = 97
$NUML_ALPHABET = 26

function Caesar-Cipher {
  param (
    [Parameter(Mandatory=$true)]
    [string]$text,
    [Parameter(Mandatory=$true)]
    [int]$shift,
    [Parameter(Mandatory=$true)]
    [string]$cryptFlag
  )

  $result = ""

  if ($cryptFlag -eq "e") {
    for ($i=0; $i -lt $text.Length; $i++) {
      $char = $text[$i]
      if ($char -match "[A-Z]") {
        $result += [char](($char.ToCharArray() -as [int[]])[0] + $shift - $ORDVAL_A % $NUML_ALPHABET + $ORDVAL_A)
      }
      elseif ($char -match "[a-z]") {
        $result += [char](($char.ToCharArray() -as [int[]])[0] + $shift - $ORDVAL_a % $NUML_ALPHABET + $ORDVAL_a)
      }
      else {
        $result += $char
      }
    }
  }
  elseif ($cryptFlag -eq "d") {
    for ($i=0; $i -lt $text.Length; $i++) {
      $char = $text[$i]
      if ($char -match "[A-Z]") {
        $result += [char](($char.ToCharArray() -as [int[]])[0] - $shift - $ORDVAL_A % $NUML_ALPHABET + $ORDVAL_A)
      }
      elseif ($char -match "[a-z]") {
        $result += [char](($char.ToCharArray() -as [int[]])[0] - $shift - $ORDVAL_a % $NUML_ALPHABET + $ORDVAL_a)
      }
      else {
        $result += $char
      }
    }
  }
  else {
    Write-Output "Error: Invalid crypt option"
  }

  Write-Output "Result is: $result"
}

function ord {
  [int][char]$input
}

# Rest of the functions (Vigenere-Cipher, Beaufort-Cipher, and main) can be implemented in a similar way
