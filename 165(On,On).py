class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1List = version1.split(".")
        ver2List = version2.split(".")
        k1 = len(ver1List)
        k2 = len(ver2List)
        k = min(k1, k2)
        for i in range(k):
            if int(ver1List[i]) > int(ver2List[i]):
                return 1
            if int(ver1List[i]) < int(ver2List[i]):
                return -1
        
        if k1 > k2:
            for i in range(k1-k):
                if int(ver1List[k-i]) > 0:
                    return 1
        else:
            for i in range(k2-k):
                if int(ver2List[k-i]) > 0:
                    return -1
        return 0

