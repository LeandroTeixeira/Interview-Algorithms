let [forward, down, up] = ["forward", "down", "up"];

function solution (movements) {
    let [depth, position] = [0,0];
    for (let i = 0; i < movements.length; i++) {
        switch (movements[i][0]) {
            case "up":
                depth -= movements[i][1];
                break;
            case "down":
                depth += movements[i][1];
                break;
            case "forward":
                position += movements[i][1];
                break;
        }
     }
    return position*depth ;
}

