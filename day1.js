function solve(input) {
  return (input + input.charAt(0))
    .split('')
    .map(Number)
    .reduce((sum, acc, i, a) => acc === a[i - 1] ? sum + acc : sum, 0)
}

