class Solution:
    def checkValidString(self, s: str) -> bool:
        countAstrik , countLeft = 0, 0
        stackAstrik = []
        stackleft = []
        for i,char in enumerate(s):
            if (countAstrik ==0 and countLeft == 0) and char==")":
                return False
            elif char == ")":
                if countLeft >0:
                    countLeft-=1
                    stackleft.pop()
                else:
                    countAstrik-=1
                    stackAstrik.pop()
            else:
                if char =="(":
                    countLeft+=1
                    stackleft.append(i)
                else:
                    countAstrik +=1
                    stackAstrik.append(i)
        while stackleft:
            if len(stackAstrik) == 0:
                return False
            elif stackleft[-1] < stackAstrik[-1]:
                stackleft.pop()
                stackAstrik.pop()
            else:
                return False
 
        return True