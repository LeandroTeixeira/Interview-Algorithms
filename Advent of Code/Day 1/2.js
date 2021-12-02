function solution (measurements) {
    let count = 0;
    for (let i = 3; i < measurements.length; i++) {
        let aux = measurements[i-1] + measurements[i-2];
        let m1 = aux + measurements[i];
        let m2 = aux + measurements[i-3];
        if (m1 > m2) count ++;
    }
    return count;
}