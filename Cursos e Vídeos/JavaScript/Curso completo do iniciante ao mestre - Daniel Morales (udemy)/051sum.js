function sum(n1,n2) {
    if (typeof n1 !== 'number' || typeof n2 !== 'number') {
        // return alert('apenas números!'); // sai da função (não funciona sempre, porque é apenas do broser)
        throw Error('sum aceita apenas números') // sai da função
    }
    return n1 + n2; // sai da função
};

// sum('a');





