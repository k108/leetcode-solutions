class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0

        while i < len(version1) or j < len(version2):
            v1 = ''
            v2 = ''

            while i < len(version1) and version1[i] == '0':
                i+=1
            while j < len(version2) and version2[j] == '0':
                j+=1

            while i < len(version1) and version1[i] != '.':
                v1 += version1[i]
                i+=1
            while j < len(version2) and version2[j] != '.':
                v2 += version2[j]
                j+=1

            if v1 == '':
                v1 = '0'
            if v2 == '':
                v2 = '0'

            print(v1, v2)
            if int(v1) < int(v2):
                return -1
            elif int(v1) > int(v2):
                return 1

            i+=1
            j+=1

        return 0    
