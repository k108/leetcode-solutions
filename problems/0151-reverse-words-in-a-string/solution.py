class Solution:
    def reverse_word(self, s, start, end):
        # adjust indexes
        for i in range(0, (end-start+1)//2):
            s[start+i],s[end-i] = s[end-i], s[start+i]

    def delete_spaces(self, s, N):
        # delete leading spaces
        for i in range(N-1, -1, -1):
            if s[i] == " ":
                s.pop()
                N-=1
            else:
                break

        # delete trailing spaces
        # take 'i' till first non-space character
        i = 0
        while i < N and s[i]==" ":
            i+=1

        write_i = 0

        while i < N:
            # if current and last character are non-space
            if not (s[i-1]==s[i]==" "):
                # keep copying characters to front
                # and keep incrementing front
                s[write_i] = s[i]
                write_i += 1
            i += 1

        # remove the left over from the end
        for _ in range(len(s)-write_i):
            s.pop()

    def reverseWords(self, s: str) -> str:
        '''
        Time Complexity : O(n)

        Space Complexity : O(1) if we don't take account of str to list conversion 
        (in fact you can't get O(1) in python because the conversion is O(n) 
        and you need it because str are immuable in python) and list to str
        '''
        s = list(s)
        N = len(s)
        # 1. reverse entire string
        # Hello World
        # dlroW olleH
        self.reverse_word(s, 0, N-1)
        
        # 2. reverse each word
        # dlroW olleH
        # World Hello
        start=0
        for j in range(N):
            if s[j]==" ":
                self.reverse_word(s, start, j-1)
                start = j+1

        self.reverse_word(s, start, N-1)
        # remove leading and trailing and in-between extra spaces
        self.delete_spaces(s, N)

        return ''.join(s)

        


        
