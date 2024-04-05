/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    let stack = []
    for (const c of s){
        if  (stack.length > 0 && Math.abs(c.charCodeAt() - stack[stack.length-1].charCodeAt()) === 32){
            stack.pop()
        }
        else {
            stack.push(c)
        }
       
    }
    return stack.join('');
};