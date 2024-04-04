/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let ans = 0, maxAns = 0;
    for (i in s){
        if (s[i] === "(") maxAns= Math.max(++ans,maxAns);
        if (s[i] === ")") ans--;
    }
    return maxAns
};