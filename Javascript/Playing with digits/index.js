function digPow(n, p) {
  return Number.isInteger(result=n.toString().split('').reduce((a,c,i)=>a+(+c)**(p+i),0)/n) ? result:-1;
}

console.log(digPow(89, 1));
console.log(digPow(92, 1));
console.log(digPow(695, 2));
console.log(digPow(46288, 3));
