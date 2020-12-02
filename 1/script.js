const fs = require('fs')
const path = require('path')

const lines = fs.readFileSync(path.resolve(__dirname, 'input.txt'), 'utf8')
const numbers = lines.trim().split('\n').map(l => parseInt(l))

for (const a of numbers) {
  for (const b of numbers) {
    if (a + b === 2020) {
      console.log(a, b, a+b, a*b)
    }
  }
}