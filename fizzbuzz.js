for(let i=0; i<=100; i++){
    let matokeo = '';
    if (i%3 === 0) matokeo += 'Fizz';
    if (i%5 === 0) matokeo += 'Buzz';
    if (i%7 === 0) matokeo += 'Bazz';
    console.log(matokeo || i);
}
