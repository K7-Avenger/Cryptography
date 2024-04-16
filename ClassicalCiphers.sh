#!/bin/bash

#still needs testing

ORDVAL_A=65
ORDVAL_a=97
NUML_ALPHABET=26

function caesar_cipher() {
  local text=$1
  local shift=$2
  local cryptFlag=$3
  result=""

  if [[ $cryptFlag == "e" ]]; then
    for (( i=0; i<${#text}; i++ )); do
      char=${text:$i:1}
      if [[ $char =~ [A-Z] ]]; then
        result+=$(echo -n "$(printf %d $(($(ord $char) + $shift - $ORDVAL_A)) $NUML_ALPHABET + $ORDVAL_A | bc)")
      elif [[ $char =~ [a-z] ]]; then
        result+=$(echo -n "$(printf %d $(($(ord $char) + $shift - $ORDVAL_a)) $NUML_ALPHABET + $ORDVAL_a | bc)")
      else
        result+=$char
      fi
    done
  elif [[ $cryptFlag == "d" ]]; then
    for (( i=0; i<${#text}; i++ )); do
      char=${text:$i:1}
      if [[ $char =~ [A-Z] ]]; then
        result+=$(echo -n "$(printf %d $(($(ord $char) - $shift - $ORDVAL_A)) $NUML_ALPHABET + $ORDVAL_A | bc)")
      elif [[ $char =~ [a-z] ]]; then
        result+=$(echo -n "$(printf %d $(($(ord $char) - $shift - $ORDVAL_a)) $NUML_ALPHABET + $ORDVAL_a | bc)")
      else
        result+=$char
      fi
    done
  else
    echo "Error: Invalid crypt option"
  fi

  echo "Result is: $result"
}

function ord() {
  printf '%d' "'$1"
}

# Rest of the functions (vigenere_cipher, beaufort_cipher, and main) can be implemented in a similar way
