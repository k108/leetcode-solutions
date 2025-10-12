class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        start = 0
        fill = 0
        for i in range(len(chars)-1):
            if chars[i] != chars[i+1]:
                diff = i - start +1
                if diff > 1:
                    diff = str(diff)
                    chars[fill] = chars[i]
                    fill += 1
                    for k in range(len(diff)):
                        chars[fill] = diff[k]
                        fill += 1
                else:
                    chars[fill] = chars[i]
                    fill += 1
                start = i+1

        diff = len(chars) - start
        if diff > 1:
            diff = str(diff)
            chars[fill] = chars[len(chars)-1]
            fill += 1
            for k in range(len(diff)):
                chars[fill] = diff[k]
                fill += 1
        else:
            chars[fill] = chars[len(chars)-1]
            fill += 1

        return fill
