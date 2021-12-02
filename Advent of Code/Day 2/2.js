let [forward, down, up] = ["forward", "down", "up"];
function solution (movements) {
    let [depth, position, aim] = [0, 0, 0];
    for (let i = 0; i < movements.length; i++) {
        switch (movements[i][0]) {
            case "up":
                aim -= movements[i][1];
                break;
            case "down":
                aim += movements[i][1];
                break;
            case "forward":
                position += movements[i][1];
                depth += movements[i][1] * aim;
                break;
        }
     }
    return position*depth ;
}
