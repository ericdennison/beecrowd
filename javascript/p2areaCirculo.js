var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let raio = parseFloat(lines.shift());
const pi = 3.14159;
const area = pi * (raio * raio);
console.log('A='+area.toFixed(4));